from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderCreateListView.as_view(), name="orders"),
    path(
        "orders/<int:order_id>/", views.OrderDetailView.as_view(), name="order_detail"
    ),
]
