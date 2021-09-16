from django.shortcuts import render,redirect

from django.contrib import messages

from mainapp.models import Appointment
from django.contrib.auth.models import User
from accounts.auth import admin_only, doctor_only
from django.contrib.auth.decorators import login_required






@login_required
def doctor_home(request):
    # doctor=Doctor.objects.count()
    patient=User.objects.filter(is_staff=0).count()
    appointment=Appointment.objects.count()
    appointments=Appointment.objects.all().order_by("-id")[:5]
    
    context={
        # 'doctor':doctor,
        'patient':patient,
        'appointment':appointment,
        'appointments':appointments


    }
    return render(request, "doctorsapp/doctorDashboard.html",context)
    
