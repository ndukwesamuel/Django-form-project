from django.forms import ModelForm

from django import forms

from .models import *




class myModelForm(ModelForm):
    class Meta:
        model= myModel
        fields= '__all__'


# class youModelForm(ModelForm):
#     class Meta:
#         model= youModel
#         fields= '__all__'
