from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.UserCreateView.as_view(), name="sign_up"),
    path("user/<int:user_id>/", views.UserDetailView.as_view(), name="user_detail"),
]
