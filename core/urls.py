from django.contrib import admin
from django.urls import path
from core.views import ResumeListView,ResumeDetailView,ResumeCreateView,ResumeUpdateView,ResumeListAPI,ResumeDetailAPI
app_name = "core"
urlpatterns = [
    path("", ResumeListView.as_view(), name="resume-list"),
    path("<int:pk>/detail/", ResumeDetailView.as_view(), name="resume-detail"),
    path("create/", ResumeCreateView.as_view(), name="resume-create"),
    path("update/<int:pk>/",ResumeUpdateView.as_view(),name="resume-update"),
    path("create/a", ResumeCreateView.as_view(template_name='template/template1.html'), name="template-one"),
    path("create/b", ResumeCreateView.as_view(template_name='template/template2.html'), name="template-two"),
    path("create/c", ResumeCreateView.as_view(template_name='template/template3.html'), name="template-three"),
    path('api/resume/',ResumeListAPI.as_view(),name='resume-list-api'),
    path('api/resume/<int:pk>/',ResumeDetailAPI.as_view(),name='resume-detail-api')
]
