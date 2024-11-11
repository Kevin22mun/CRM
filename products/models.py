from django.db import models
from base.models import BaseModel

class ProductBase(BaseModel):
    TYPE_CHOICES = [
        ('plan', 'Plan'),
        ('package', 'Recarga'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        db_table = "product_bases"

    def __str__(self):
        return f"{self.name} ({self.type})"

class ProductVariant(BaseModel):
    product_base = models.ForeignKey(ProductBase, on_delete=models.CASCADE, related_name="variants")
    data = models.CharField(max_length=50, null=True, blank=True, verbose_name="Data (GB)")
    share_data = models.BooleanField(default=False)
    minutes = models.IntegerField(null=True, blank=True)
    sms = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    portability_promo=models.CharField(max_length=50, null=True, blank=True)
    code=models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(
    max_length=20,
    choices=[('active', 'Active'), ('inactive', 'Inactive')],
    default='active'
)

    class Meta:
        db_table = "product_variants"

    def __str__(self):

        return f"{self.product_base.name} - {self.data or 'No Data'}"