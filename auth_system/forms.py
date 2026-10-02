from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
