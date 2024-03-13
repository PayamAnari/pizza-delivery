from django.contrib import admin
from .models import Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "size",
        "order_status",
        "quantity",
        "flavour",
        "created_at",
        "updated_at",
        "id",
    ]
    list_filter = ["created_at", "updated_at", "order_status", "size"]
