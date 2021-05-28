from rest_framework import viewsets
from rest_framework import permissions
from market.serializers import ProductSerializer
from market.models import Product
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-create_at")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
