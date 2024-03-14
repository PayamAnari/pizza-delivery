from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


# Create your views here.
class OrderCreateListView(generics.GenericAPIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass

    def post(self, request, order_id):
        pass


class OrderDetailView(generics.GeneriAPIView):

    def get(self, request, order_id):
        pass

    def put(self, request, order_id):
        pass
