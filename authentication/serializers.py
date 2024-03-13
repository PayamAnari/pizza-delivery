from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        label=("first name"), max_length=30, allow_blank=True
    )
    last_name = serializers.CharField(
        label=("last name"), max_length=30, allow_blank=False
    )
    username = serializers.CharField(
        label=("username"), max_length=40, allow_blank=False
    )
    email = serializers.EmailField(label=("email address"), max_length=80)
    phone_number = PhoneNumberField(
        label=("phone number"), allow_blank=False, allow_null=False
    )
    password = serializers.CharField(
        label=("password"), min_length=8, allow_blank=False, write_only=True
    )
    date_of_birth = serializers.DateField(label=("date of birth"), allow_null=True)
    delivery_address = serializers.CharField(
        label=("delivery_address"), max_length=255, allow_blank=True, allow_null=True
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

        phonenumber = User.objects.filter(username=attrs["phone_number"]).exists()

        if phonenumber:
            raise serializers.validationError(detail="User with phone number exists")

        address = User.objects.filter(username=attrs["delivery_address"]).exists()

        if address:
            raise serializers.validationError(detail="User with address exists")

        return super().validate(attrs)
