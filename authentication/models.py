from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email is required"))
        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True."))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=30, unique=True)
    last_name = models.CharField(_("last name"), max_length=30, unique=True)
    username = models.CharField(_("username"), max_length=30, unique=True)
    email = models.EmailField(_("email address"), max_length=80, unique=True)
    phone_number = PhoneNumberField(_("phone number"), unique=True)
    date_of_birth = models.DateField(_("date of birth"), unique=True, null=True)
    delivery_address = models.CharField(
        _("delivery_address"), max_length=255, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "username",
        "phone_number",
        "date_of_birth",
        "delivery_address",
    ]

    def __str__(self):
        return f"<User {self.email}"
