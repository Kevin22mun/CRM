from django.db import models
from base.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Network(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_variant = models.ForeignKey('products.ProductVariant', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('pending', 'Pending'),
            ('suspended', 'Suspended')
        ]
    )
    is_esim = models.BooleanField(default=False)
    qr_code = models.CharField(max_length=255, null=True, blank=True)
    sim_id = models.CharField(max_length=50, null=True, blank=True)
    contract_id = models.CharField(max_length=50, null=True, blank=True)
    msisdn = models.CharField(max_length=20, null=True, blank=True)
    iccid = models.CharField(max_length=20, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)
    membership_number = models.CharField(max_length=50, null=True, blank=True)
    two_fa_code = models.CharField(max_length=10, null=True, blank=True)
    two_fa_code_expiry = models.DateTimeField(null=True, blank=True)
    is_portable = models.BooleanField(default=False)
    
    class Meta:
        db_table = "networks"

    def __str__(self):
        return f"Network {self.msisdn} ({self.status})"

    
class NetworkSubscription(BaseModel):
    network = models.ForeignKey('networks.Network', on_delete=models.CASCADE, null=True, blank=True)
    product_variant = models.ForeignKey('products.ProductVariant', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        db_table = "networks_subscriptions"

    def __str__(self):
        return f"{self.network.msisdn} Subscription ({self.start_date} - {self.end_date})"
