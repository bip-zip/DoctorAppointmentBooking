from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appuser')
    profile_pic= models.ImageField(upload_to='user_pics', null=True, blank=True)
    address= models.CharField(max_length=255, null=True)
    age= models.PositiveIntegerField(null=True)
    contact= models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.user.username

    @property
    def joined_date(self):
        return self.user.date_joined


    @property
    def imageUrl(self):
        try:
            url=self.profile_pic.url
        except:
            url=''
        return url

class Specilization(models.Model):
    specilization_type=models.CharField(max_length=255, null=False)
    problem_related=models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.specilization_type


class DoctorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    dob= models.DateField(null=True)
    total_experience_years= models.PositiveIntegerField(null=True)
    address= models.CharField(max_length=255, null=True)
    contact= models.CharField(max_length=10, null=True)
    maximum_degree= models.ImageField(upload_to='doctors_degree',null=False)
    specilization=models.ForeignKey(Specilization,null=False, on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='doctors_pics', null=True, blank=True)
    admin_approve=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    @property
    def imageUrl(self):
        try:
            url=self.profile_pic.url
        except:
            url=''
        return url

    def save(self, *args, **kwargs):
        if self.admin_approve == True:
            self.user.is_active = True
            self.user.is_staff = True
            self.user.save()
        else:
            self.user.is_active = False
            self.user.is_staff = False
            self.user.save()
        super(DoctorUser, self).save(*args, **kwargs)

