from django.db import models
from django.contrib.auth.models import User
from auth_system.models import CustomUser
import os
# Create your models here.
class Resume(models.Model):
    choose = [
        ('resume/resume1.html', 'Standard Resume'),
        ('resume/resume2.html', 'Modern Resume'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True,blank=True,null=True,default=' ')
    full_name = models.CharField(blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    occupation = models.CharField(max_length=100,null=True,blank=True)
    experience = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    template = models.ForeignKey('ResumeTemplate',on_delete=models.DO_NOTHING,blank=True,null=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        ordering = ['-created_at']
class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100,null=True)
    file = models.FileField(upload_to='core/templates/template/',null=True,blank=True)
    
    def __str__(self):
        return self.name
    def delete(self,*args,**kwargs):
        if self.file:
            file_name = self.file.path
        if os.path.exists(file_name):
            os.remove(self.file.path)
        return super().delete(*args,**kwargs)

