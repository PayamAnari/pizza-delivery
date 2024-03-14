from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(max_length=20, default="PENDING")
    quantity = serializers.IntegerField()
