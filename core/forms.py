from django import forms
from .models import Resume,ResumeTemplate

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title','full_name','age','description','occupation','experience']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
        }
class TemplateForm(forms.Form):
    template = forms.ModelChoiceField(
    required=False,
    label='Шаблони',
    queryset=ResumeTemplate.objects.all(),
    empty_label = '---------',
    initial=ResumeTemplate.objects.first(),
    )