from django.contrib import admin
from .models import Order, Purchase, Shipment,ShippingRate

# Register your models here.
admin.site.register(Order)
admin.site.register(Purchase)
admin.site.register(Shipment)
admin.site.register(ShippingRate)