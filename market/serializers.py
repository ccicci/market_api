from rest_framework import serializers
from market.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'category', 'status', 'create_at', 'update_at']
