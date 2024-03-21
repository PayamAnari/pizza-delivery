from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema


User = get_user_model()


# Create your views here.
class OrderCreateListView(generics.GenericAPIView):

    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    # @swagger_auto_schema(
    #     operation_summary="Get all orders",
    # )
    # def get(self, request):
    #     orders = Order.objects.all()
    #     serializer = self.serializer_class(instance=orders, many=True)

    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new order",
    )
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAllView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailAllSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all orders")
    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get an order by id")
    def get(self, request, order_id):

        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an order by id")
    def put(self, request, order_id):

        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "Order updated successfully",
                    "order": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete an order by id")
    def delete(self, request, order_id):

        order = get_object_or_404(Order, pk=order_id)

        order.delete()
        return Response(
            data={"message": "Order deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="Update an order status by id")
    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        data = request.data

        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "Order status updated successfully",
                    "order": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrdersView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="Get all orders by user id")
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        orders = Order.objects.all().filter(customer=user)

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrderDetail(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary="Get an order by user id and order id")
    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = get_object_or_404(Order, pk=order_id, customer=user)

        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
