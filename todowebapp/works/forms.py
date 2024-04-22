from django import forms
from django.contrib.auth.models import User
from works.models import Project,Todo

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']

class LoginForm(forms.Form):
    username= forms.CharField()
    password= forms.CharField()

class ProjectaddingForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title']

class TodoaddingForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title', 'description', 'status']