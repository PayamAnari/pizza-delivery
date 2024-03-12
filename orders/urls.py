from django.urls import path
from . import views

urlpatterns = [
    path("", views.HellOrderView.as_view(), name="hello_auth"),
]
