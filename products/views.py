from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductBase
from .serializers import ProductBaseSerializer

# Create your views here.
class ProductListView(APIView):
    def get(self, request):
        products = ProductBase.objects.prefetch_related('variants').all()
        serializer = ProductBaseSerializer(products, many=True)
        return Response(serializer.data)
