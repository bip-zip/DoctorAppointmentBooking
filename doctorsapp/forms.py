from django import forms
from mainapp.models import Availabity

class AvaiForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model=Availabity
        fields=['date','time']





