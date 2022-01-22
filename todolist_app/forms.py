from dataclasses import field
from pyexpat import model
from django import forms
from . models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['task', 'completed']