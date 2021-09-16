from django.db import models
from django.contrib.auth.models import User
from doctorsapp.models import Doctor



class Appointment (models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    phonenumber=models.CharField(max_length=15, null=True)
    email=models.EmailField( null=True)
    age=models.PositiveIntegerField( null=True)
    address=models.CharField(max_length=200, null=True)
    date=models.CharField(max_length=20, null=True)
    desc=models.TextField( null=True)
    seen=models.BooleanField(default=False)
    response=models.CharField(max_length=500, null=True, blank=True)
    appointmentdate=models.CharField(max_length=20, null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True)
    appliedon=models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return (self.name)







