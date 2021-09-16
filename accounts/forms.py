from accounts.models import AppUser
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AppUser, DoctorUser
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']

class ProfileForm(ModelForm):
    class Meta:
        model=AppUser
        fields=['contact','age','address','profile_pic']

class DoctorForm(ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model=DoctorUser
        fields='__all__'
        exclude=('user','admin_approve')

class LoginForm(forms.Form):
    username = forms.CharField()
    password =  forms.CharField(widget=forms.PasswordInput)


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True,label='First Name')
    last_name=forms.CharField(required=True,label='Last Name')

    class Meta:
        model = User
        fields = ('first_name','last_name',"username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

