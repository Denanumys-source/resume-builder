from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
# Create your models here.

class CustomUser(AbstractUser):
    choices = (
        ('user','User'),
        ('admin','Admin')
    )
    role = models.CharField(default='user',choices=choices)
    def is_admin_role(self):
        return self.role == 'admin' or self.is_staff or self.is_superuser
    def __str__(self):
        return self.username


