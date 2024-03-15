from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default="PENDING")
    quantity = serializers.IntegerField()
    flavour = serializers.CharField(max_length=20)

    class Meta:
        model = Order
        fields = ["size", "order_status", "quantity", "flavour"]


class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.CharField(default="PENDING")
    quantity = serializers.IntegerField()
    flavour = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
