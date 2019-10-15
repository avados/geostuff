from django import forms
from .models import Step
from django.forms import ModelForm


class StepForm(ModelForm):
    class Meta:
        model = Step
        fields = ['id', 'name', 'point']
