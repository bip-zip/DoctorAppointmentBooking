from django import forms
from .models import Doctor
from django.forms import ModelForm

class DoctorForm(ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'






