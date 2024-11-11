# payments/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from services.payments.openpay_services import OpenpayService
import requests
import logging

logger = logging.getLogger('openpay_webhook')

openpay_service = OpenpayService()

@csrf_exempt
def unified_charge(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_method = data.get("payment_method")  # "CARD" o "STORE"
        
        # Información del cliente y orden
        customer_id = data.get("customer").get("id")
        name = data.get("customer").get("name")
        email = data.get("customer").get("email")
        order_data = {
            "amount": data.get("amount"),
            "description": data.get("description"),
        }

        try:
            # Cobro con tarjeta
            if payment_method == "CARD":
                card_data = {
                    "source_id": data.get("source_id"),  # ID de la tarjeta
                    "device_session_id": data.get("device_session_id"),
                }
                payment = openpay_service.charge_with_card(customer_id, {**order_data, **card_data})

            # Cobro en tienda
            elif payment_method == "STORE":
                store_data = {
                    "method": "store",
                    "amount": data.get("amount"),
                    "description": data.get("description"),
                    "customer": {
                        "id": customer_id,
                        "name": name,
                        "email": email
                    }
                }
                payment = openpay_service.charge_in_store(customer_id, store_data)
            else:
                return JsonResponse({"error": "Método de pago no válido"}, status=400)

            return JsonResponse(payment)

        except requests.exceptions.HTTPError as e:
            error_data = e.response.json()
            logger.error("HTTP Error: %s", error_data)
            return JsonResponse({"error": error_data}, status=e.response.status_code)

        except Exception as e:
            logger.error("Unexpected error: %s", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def openpay_webhook(request):
    if request.method == 'POST':
        try:
            event_data = json.loads(request.body)
            logger.info("Webhook received from Openpay: %s", event_data)

            event_type = event_data.get("type")
            if event_type == "charge.succeeded":
                process_successful_charge(event_data)
            elif event_type == "charge.failed":
                process_failed_charge(event_data)
            elif event_type == "charge.cancelled":
                process_cancelled_charge(event_data)
            else:
                logger.warning("Unhandled event type: %s", event_type)

            return JsonResponse({"status": "success"}, status=200)

        except json.JSONDecodeError:
            logger.error("Invalid JSON received in webhook.")
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except Exception as e:
            logger.error("Error processing Openpay webhook: %s", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)


def process_successful_charge(event_data):
    transaction_id = event_data["transaction"]["id"]
    amount = event_data["transaction"]["amount"]
    logger.info("Charge succeeded for transaction ID: %s, amount: %s", transaction_id, amount)
  


def process_failed_charge(event_data):
    transaction_id = event_data["transaction"]["id"]
    error_message = event_data["transaction"].get("error_message", "No error message provided")
    logger.warning("Charge failed for transaction ID: %s, error: %s", transaction_id, error_message)
   


def process_cancelled_charge(event_data):
    transaction_id = event_data["transaction"]["id"]
    logger.info("Charge cancelled for transaction ID: %s", transaction_id)
    