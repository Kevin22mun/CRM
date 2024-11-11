from django.db import models
from base.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    network = models.ForeignKey('networks.Network', on_delete=models.CASCADE, null=True, blank=True)
    product_variant = models.ForeignKey('products.ProductVariant', on_delete=models.CASCADE)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_type=models.CharField(max_length=50, choices=[('multilinea', 'Multilinea'), 
                                                        ('invitacion', 'Invitación'),('renovacion', 'Renovación'), ('recarga', 'Recarga')], null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('canceled', 'Canceled'),
            ('in_process', 'In Process'),
            ('shipped', 'Shipped'),
        ]
    )

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class Purchase(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    invoice_id = models.CharField(max_length=255, null=True, blank=True)  # Factura única para la compra completa

    class Meta:
        db_table = "purchases"

    def __str__(self):
        return f"Purchase {self.id} - User {self.user.id}"



class Shipment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="shipments")
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    carrier = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('in_transit', 'In Transit'),
            ('delivered', 'Delivered'),
            ('returned', 'Returned'),
        ]
    )

    class Meta:
        db_table = "shipments"

    def __str__(self):
        return f"Shipment {self.id} - Order {self.order.id}"


class ShippingRate(BaseModel):
    SHIPPING_TYPE_CHOICES = [
        ('initial', 'Envío inicial'),
        ('replacement', 'Reposición'),
        ('defective_replacement', 'Reposición por defecto'),
        ('lost', 'Pérdida/robo'),
    ]

    shipping_type = models.CharField(max_length=50, choices=SHIPPING_TYPE_CHOICES)
    product_type = models.CharField(max_length=20, choices=[('sim', 'SIM'), ('esim', 'eSIM')], null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)  # Opcional si usas tarifas por región
    rate = models.DecimalField(max_digits=10, decimal_places=2)  # Costo de envío
    is_free = models.BooleanField(default=False)  # Para casos donde el envío es gratuito

    class Meta:
        db_table = "shipping_rates"

    def __str__(self):
        return f"{self.get_shipping_type_display()} - {self.product_type or 'General'}: ${self.rate}"
