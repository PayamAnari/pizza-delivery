from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(("first name"), max_length=30, allow_blank=True)
    last_name = serializers.CharField(("last name"), max_length=30, allow_blank=False)
    username = serializers.CharField(("username"), max_length=40, allow_blank=False)
    email = serializers.EmailField(("email address"), max_length=80, unique=True)
    phone_number = PhoneNumberField(
        ("phone number"), allow_blank=False, allow_null=False
    )
    password = serializers.CharField(
        ("password"), min_length=8, allow_blank=False, write_only=True
    )
    date_of_birth = serializers.DateField(("date of birth"), allow_null=True)
    delivery_address = serializers.CharField(
        ("delivery_address"), max_length=255, allow_blank=True, allow_null=True
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "password",
            "date_of_birth",
            "delivery_address",
        ]

    def validate(self, attrs):

        username = User.objects.filter(username=attrs["username"]).exists()

        if username:
            raise serializers.ValidationError(detail="User with username exists")

        email = User.objects.filter(username=attrs["email"]).exists()

        if email:
            raise serializers.validationError(detail="User with email exists")

        phone_number = User.objects.filter(username=attrs["phone_number"]).exists()

        if phone_number:
            raise serializers.validationError(detail="User with phone number exists")

        return super().validate(attrs)
