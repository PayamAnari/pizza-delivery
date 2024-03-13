from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Order(models.Model):

    SIZES = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA_LARGE", "extra_large"),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
