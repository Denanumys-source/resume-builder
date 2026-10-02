from django.contrib import admin
from django.urls import path
from auth_system.views import AccountLoginView, AccountRegisterView, AccountLogoutView
app_name = "accounts"
urlpatterns = [
    path("register/", AccountRegisterView.as_view(), name="register"),
    path("login/", AccountLoginView.as_view(), name="login"),
    path("logout/", AccountLogoutView.as_view(), name="logout"),
]
