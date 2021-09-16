from django.contrib import admin
from .models import AppUser,DoctorUser,Specilization



admin.site.register(AppUser)
admin.site.register(DoctorUser)
admin.site.register(Specilization)

