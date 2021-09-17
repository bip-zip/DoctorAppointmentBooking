from mainapp.models import Appointment
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        widgets = {
            'response': forms.Textarea(attrs={'cols': 100, 'rows': 4}),
        }
        fields=['response']