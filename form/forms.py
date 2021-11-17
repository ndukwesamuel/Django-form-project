from django import forms
from django.db.models import fields
from django.forms.models import ALL_FIELDS

from django.forms import ModelForm
from form.models import myModel

class myModelForm(ModelForm):
    class Meta:
        model = myModel
        fields = '__all__'