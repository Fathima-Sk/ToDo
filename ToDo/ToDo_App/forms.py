from django import forms
from django.contrib.auth.models import User
from ToDo_App.models import Task


class register(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class sign_in(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    

class Task_form(forms.ModelForm):
    class Meta:
        model= Task
        fields=['name']