from django.db import models
from base.models import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(null=True, blank=True)
    contact_phone_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = "user_profiles"

    def __str__(self):
        return f"Profile for User {self.user.username}"

class BankDetail(BaseModel):  
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="bank_details")
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    clabe = models.CharField(max_length=18, null=True, blank=True)

    class Meta:
        db_table = "bank_details"

    def __str__(self):
        return f"Bank Details for User {self.user.id}"

class Address(BaseModel):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=255)
    exterior_number = models.CharField(max_length=50)
    interior_number = models.CharField(max_length=50, null=True, blank=True)
    neighborhood = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    municipality = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address_type = models.CharField(max_length=20, choices=[('residential', 'Residential'), ('fiscal', 'Fiscal')])

    class Meta:
        db_table = "addresses"

    def __str__(self):
        return f"Address {self.id} - {self.address_type}"

class TaxData(BaseModel):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="tax_data")
    rfc = models.CharField(max_length=13)
    cfdi_use = models.CharField(max_length=10)
    fiscal_regime = models.CharField(max_length=50)
    tax_zip_code = models.CharField(max_length=10)

    class Meta:
        db_table = "tax_data"
        
    def __str__(self):
        return f"Tax Data for User {self.user.id}"
