from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterForm,LoginForm

# Create your views here.
class AccountLoginView(LoginView):
    template_name = 'auth_system/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:resume-list')
class AccountRegisterView(CreateView):
    template_name = 'auth_system/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('core:resume-list')
    def form_valid(self,form):
        response = super().form_valid(form)
        login(self.request,self.object)
        return response
class AccountLogoutView(LogoutView):
    success_url = reverse_lazy('core:resume-list')
    pass
