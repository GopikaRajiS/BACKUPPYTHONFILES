from django import forms
from .models import Lmodel

class Limodel(forms.ModelForm):
    class Meta:
        model=Lmodel
        fields=[
            "title",
            "description",
        ]