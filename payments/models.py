from django.db import models
from base.models import BaseModel


class Payment(BaseModel):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    payment_form = models.CharField(
        max_length=20,
        choices=[
            ('01', 'Efectivo'),
            ('03', 'Transferencia Electrónica'),
            ('04', 'Tarjeta de Crédito'),
            ('28', 'Tarjeta de Débito'),
        ]
    )
    payment_method = models.CharField(
        max_length=3,
        choices=[
            ('PUE', 'Pago en una sola exhibición'),
            ('PPD', 'Pago en parcialidades o diferido')
        ]
    )

    payment_date = models.DateField()
    payment_reference = models.CharField(max_length=255, null=True, blank=True)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    payment_url = models.CharField(max_length=500, null=True, blank=True)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Saldo restante después del pago")
    due_date = models.DateField(null=True, blank=True, help_text="Fecha límite de pago para pagos PPD")

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
            ('rejected', 'Rejected'),
            ('refunded', 'Refunded')
        ],
        default='pending'
    )

    class Meta:
        db_table = "payments"

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.amount} ({self.status})"
