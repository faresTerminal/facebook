from django import forms
from django.db import models


from fishing.models import articles
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class createForm(forms.ModelForm):
   
    class Meta:
        model = articles
        fields = [
           
            'title',
       
           
            
        ]
