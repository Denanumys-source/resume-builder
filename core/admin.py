from django.contrib import admin
from .models import Resume, ResumeTemplate
# Register your models here.
@admin.register(Resume)
class Resume(admin.ModelAdmin):
    list_display = ('user', 'title', 'occupation', 'created_at')
    search_fields = ('user', 'title')

@admin.register(ResumeTemplate)
class Template(admin.ModelAdmin):
    list_display = ('name','file')
