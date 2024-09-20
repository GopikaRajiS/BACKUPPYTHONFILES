from django import forms
from studentapp.models import student


class studentsForm(forms.ModelForm):
    registernumber = forms.IntegerField(max_value=300)
    firstname = forms.CharField(label="enter first name", max_length=50)
    lastname = forms.CharField(label="enter last name", max_length=100)

class stuForm(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"