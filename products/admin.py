from django.contrib import admin
from .models import ProductBase, ProductVariant

# Register your models here.
admin.site.register(ProductBase)
admin.site.register(ProductVariant)
