# payments/urls.py
from django.urls import path
from .views import unified_charge, openpay_webhook

urlpatterns = [
    path('charge/', unified_charge, name='unified_charge'),
    path('webhook/', openpay_webhook, name='openpay_webhook'),
]