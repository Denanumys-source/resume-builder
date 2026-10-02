from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from .models import Resume,ResumeTemplate
from .forms import ResumeForm,TemplateForm
from django.urls import reverse_lazy
from .serializers import ResumeSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from auth_system.mixins import AdminRequiredMixin
# Create your views here.
class ResumeListView(ListView):
    model = Resume
    template_name = 'core/list.html'
    context_object_name = 'resume'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'core/detail.html'
    context_object_name = 'resume'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['t_con'] = '2'
        return context
class ResumeCreateView(LoginRequiredMixin,CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'form/form2.html'
    success_url = reverse_lazy('core:resume-list')
    context_object_name = 'resume'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tform'] = TemplateForm(self.request.GET)
        context['t_con'] = '1'
        return context
    def get(self, request, *args, **kwargs):
        t_form = TemplateForm(self.request.GET)
        if t_form.is_valid():
            template = t_form.cleaned_data.get('template')
            if template:
                self.template_name = template.file.path
        return super().get(request, *args, **kwargs)
    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.template = get_object_or_404(ResumeTemplate, name=self.request.GET.get('template'))
        return super().form_valid(form)
class ResumeUpdateView(LoginRequiredMixin,UpdateView):
    model = Resume
    template_name = 'form/form2.html'
    success_url = reverse_lazy('core:resume-list')
    form_class = ResumeForm
    context_object_name = 'resume'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ResumeListAPI(ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer