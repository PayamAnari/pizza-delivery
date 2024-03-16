from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


class UserCreateView(generics.GenericAPIView):

    serializer_class = serializers.UserCreationSerializer

    @swagger_auto_schema(
        operation_summary="Create a new user",
    )
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all users")
    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(instance=users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserDetailView(generics.GenericAPIView):

    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get a user by id")
    def get(self, request, user_id):

        user = User.objects.get(pk=user_id)
        serializer = self.serializer_class(instance=user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update a user by id")
    def put(self, request, user_id):

        user = User.objects.get(pk=user_id)

        serializer = self.serializer_class(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data={
                    "message": "User updated successfully",
                    "user": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete a user by id")
    def delete(self, request, user_id):
        user = User.objects.get(pk=user_id)
        user.delete()
        return Response(
            data={"message": "User deleted successfully"}, status=status.HTTP_200_OK
        )
