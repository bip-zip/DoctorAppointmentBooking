from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from accounts.auth import *
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import Specilization, DoctorUser, AppUser
from django.contrib import messages

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


from django.core.mail import send_mail
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
        time=request.POST.get("time")
        doctor=request.POST.get("doctor")
        ac_doctor=DoctorUser.objects.get(id=doctor)

        appform=Appointment(user=user, name=name,phonenumber=number,email=email,age=age,address=address,date=date,desc=desc, time=time, doctor=ac_doctor)
        appform.save()
        
        message1=('Hello,Dr. '+ str(ac_doctor.user.first_name) + str(ac_doctor.user.last_name) + ' someone has booked appointment on'+ str(date) + ',' + str(time) +' with you. Check your profile for more information.' )
        send_mail('Appointment Nepal - Appointment alert!',message1,'herohiralaal14@gmail.com',[ac_doctor.user.email],fail_silently=False)

        message=('Hello, Dear '+user.first_name + ' ' + user.last_name +' you appointment is booked with Dr. '+ str(ac_doctor.user.first_name) + str(ac_doctor.user.last_name) + ' on '+ str(date) + ',' + str(time) +'. Thank you.' )
        send_mail('Appointment Nepal - Booked Success!',message,'herohiralaal14@gmail.com',[user.email],fail_silently=False)

        messages.add_message(request, messages.SUCCESS, 'Appointment booked successfully!')
        return redirect("mainapp:home")
    else:
        problems=Specilization.objects.all()
        context={'active_appointmet':'active','problems':problems}
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

from django.template.loader import render_to_string
def checkAvaibility(request):
    if request.method == "POST":
        problem=request.POST['problem']
        date=request.POST['date']
        time=request.POST['time']
        print(problem,date,time)

        doctors= DoctorUser.objects.filter(specilization=(Specilization.objects.get(id=problem)))
        avai=Availabity.objects.filter(doctor__in=doctors,date=date,time=time)

        t=render_to_string('mainapp/avai.html',{'data':avai},request=request)
        return JsonResponse({'data':t})
     


        
        # if checkRight.count() > 0 :
        #     checkRight.delete()
        #     actualVote=answer.actual_vote
        #     return JsonResponse({'bool':True,'actualVote':actualVote})

        # elif checkWrong.count() > 0 :
        #     checkWrong.delete()
        #     RightPoint.objects.create(
        #         answer=answer,
        #         user=user)
        #     actualVote=answer.actual_vote
        #     return JsonResponse({'bool':True,'actualVote':actualVote})
        # else:
        #     RightPoint.objects.create(
        #         answer=answer,
        #         user=user)
        #     actualVote=answer.actual_vote
        #     return JsonResponse({'bool':True,'actualVote':actualVote})