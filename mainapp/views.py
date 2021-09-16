from django.shortcuts import render
from django.http import HttpResponse
from accounts.auth import *
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):
    context={'active_home':'active'}
    return render(request,'mainapp/home.html',context)

def about(request):
    context={'active_about':'active'}
    return render(request,'mainapp/About.html',context)

def profile(request):
    user=request.user
    appointments=Appointment.objects.filter(user=user)
    context={
        'appointments':appointments
    }
    return render(request,'mainapp/profile.html',context)

def contact(request):
    context={'active_contact':'active'}
    return render(request,'mainapp/contact.html',context)

@user_only 
@login_required
def appointment(request):
    if request.method == "POST":
        user=request.user
        name=request.POST.get("fullname")
        number=request.POST.get("phonenumber")
        email=request.POST.get("email")
        age=request.POST.get("age")
        address=request.POST.get("address")
        date=request.POST.get("date")
        desc=request.POST.get("desc")
        appform=Appointment(user=user, name=name,phonenumber=number,email=email,age=age,address=address,date=date,desc=desc)
        appform.save()
        return redirect("mainapp:home")
    else:
        context={'active_appointmet':'active'}
        return render(request,'mainapp/appointmentTable.html',context)


@user_only
@login_required
def oldappointment(request):
    user=request.user
    appointments=Appointment.objects.filter(user=user)
    context={
        'appointments':appointments
    }
    return render(request,'mainapp/oldAppointment.html',context)


def response(request,id):

     
    appointment=Appointment.objects.get(id=id)
    
    
    context={
        'appointment':appointment,
    }
    return render(request,'mainapp/appointResponse.html',context)


