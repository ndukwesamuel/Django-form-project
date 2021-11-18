from django.forms import ModelForm

from django import forms

from .models import *




class myModelForm(forms.ModelForm):
    class Meta:
        model= myModel
        fields= '__all__'

