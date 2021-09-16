from django.db import models
from django.contrib.auth.models import User
from accounts.models import DoctorUser

# times=(('09:00 am - 09:30 am','09:00 am - 09:30 am'),
#                 ('psychiatrist','Psychiatrist'),
#                 ('surgeon','Surgeon'),
#                 ('anesthesiologist','Anesthesilogist'),
#                 ('neurologist','Neurologist'),
#                 ('pulmonologist','Pulmonologist'),
#                 ('dermatologist','Dermatologist'),
#                 ('cardiologist','Cardiologist'))

times=(('09:00 am - 09:30 am','09:00 am - 09:30 am'),
               ('09:30 am - 10:00 am','09:30 am - 10:00 am'),
               ('10:00 am - 10:30 am','10:00 am - 10:30 am'),
               )

class Appointment (models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    phonenumber=models.CharField(max_length=15, null=True)
    email=models.EmailField( null=True)
    age=models.PositiveIntegerField( null=True)
    address=models.CharField(max_length=200, null=True)
    desc=models.TextField( null=True)
    date=models.DateField(null=True)
    time= models.CharField(max_length=20, null=True,choices=times )
    seen=models.BooleanField(default=False)
    response=models.TextField(null=True)
    
    doctor=models.ForeignKey(DoctorUser,on_delete=models.CASCADE, null=True)
    applied_date=models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return (self.name)


class Availabity(models.Model):
    doctor=models.ForeignKey(DoctorUser, on_delete=models.CASCADE)
    date= models.DateField(null=False)
    time= models.CharField(max_length=20, null=True,choices=times )
    booked= models.BooleanField(default=False)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return str(self.doctor.user.first_name +' '+ self.doctor.user.last_name + ' '+ str(self.date) +' '+ str(self.time) )



