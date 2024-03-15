from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Orders
from . import serializers


# Create your views here.
class OrderCreateListView(generics.GenericAPIView):

    serializer_class = serializers.OrderCreationSerializer

    def get(self, request):
        orders = Orders.objects.all()
        serializer = self.serializer_class(instance=orders)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass


class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass

    def post(self, request, order_id):
        pass


class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass

    def put(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass
