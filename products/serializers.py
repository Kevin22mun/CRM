from rest_framework import serializers
from .models import ProductBase, ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "data",
            "share_data",
            "minutes",
            "sms",
            "duration",
            "price",
            "portability_promo",
            "code",
            "status",
            "product_base",
        ]

class ProductBaseSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = ProductBase
        fields = [
            "id",
            "name",
            "type",
            "variants", 
        ]
