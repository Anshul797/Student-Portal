from django import forms
from college.models import Student
from django.urls.base import reverse_lazy
from captcha.fields import CaptchaField
class StudentForm(forms.ModelForm):
    skills = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Phone No'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone No'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'EMail'}))
    captcha = CaptchaField()
    class Meta:
        model = Student
        fields = ['skills', 'phone_no', 'email','captcha']