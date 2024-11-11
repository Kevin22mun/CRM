import os
import requests
import base64

class OpenpayService:
    def __init__(self):
        self.api_key = os.getenv('OPENPAY_SK')
        self.merchant_id = os.getenv('OPENPAY_ID')
        self.base_url = os.getenv('OPENPAY_DASHBOARD_PATH')
        self.environment = os.getenv('OPENPAY_ENV', 'true').lower() == 'true'  # True for sandbox, False for production

    def _get_headers(self):
        # Codifica el API key en Base64 con el formato correcto 'api_key:'
        headers = {
            'Authorization': f'Basic {base64.b64encode(f"{self.api_key}:".encode()).decode()}',
            'Content-Type': 'application/json'
        }
        print("Headers:", headers)  # Debug
        return headers


    def charge_with_card(self, customer_id, charge_data):
        url = f"{self.base_url}{self.merchant_id}/charges"
        charge_data['customer'] = {"id": customer_id}
        response = requests.post(url, json=charge_data, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    # openpay_service.py
    def charge_in_store(self, customer_id, store_data):
        url = f"{self.base_url}{self.merchant_id}/charges"
        store_data['customer'] = {
            "id": customer_id,
            "name": store_data.get("customer", {}).get("name"),
            "email": store_data.get("customer", {}).get("email"),
            "phone_number": store_data.get("customer", {}).get("phone_number")
        }
        try:
            response = requests.post(url, json=store_data, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


