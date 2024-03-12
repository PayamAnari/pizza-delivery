from django.urls import path
from . import views

urlpattern = [
    path("", views.HelloAuthView.as_view(), name="hello-auth"),
]
