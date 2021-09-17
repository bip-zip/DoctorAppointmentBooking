from django.shortcuts import render,redirect

from django.contrib import messages

from mainapp.models import Appointment
from django.contrib.auth.models import User
from accounts.auth import admin_only, doctor_only
from django.contrib.auth.decorators import login_required
from accounts.models import DoctorUser
from mainapp.models import Availabity



@login_required
def doctor_home(request):
    user=request.user
    doctor=DoctorUser.objects.get(user=user)
    all_appointments=Appointment.objects.filter(doctor=doctor).count()
    completed=Appointment.objects.exclude(doctor=doctor, response__isnull=True).count()
    not_responded=Appointment.objects.filter(doctor=doctor, response=None).count()
    appointments=Appointment.objects.filter(doctor=doctor).order_by("-id")[:5]
    
    context={
        'all_appointments':all_appointments,
        'completed':completed,
        'not_responded':not_responded,
        'appointments':appointments
    }
    return render(request, "doctorsapp/doctorDashboard.html",context)
    

from django.views import View
from django.views.generic import UpdateView
from .forms import AvaiForm
class AddAvaibality(View):
    def get(self, request, *args, **kwargs):
        
        form=AvaiForm
        doctor=DoctorUser.objects.get(user=(self.request.user))
        all_avai=Availabity.objects.filter(doctor=doctor).order_by('-id')
        return render(request,'doctorsapp/availabity_form.html',{'form':form,'all_avai':all_avai})
    
    def post(self, request, *args, **kwargs):
        doctor=DoctorUser.objects.get(user=(request.user))
        form=AvaiForm(request.POST)
        if form.is_valid():
            ok=form.save(commit=False)
            ok.doctor=doctor
            form.save(commit=True)
            messages.add_message(request, messages.SUCCESS, 'Availability added successfully!')

            return redirect('doctorsapp:addavai')
        else:
            messages.add_message(request, messages.ERROR, 'Availability already exists!')
            return redirect('doctorsapp:addavai')
    

# def Updateavailability(request,id):
   
#     avai=Availabity.objects.get(id=id)
#     form1=AvaiForm(instance=avai)
#     if request.method == 'POST':
#         if form1.is_valid():
            
            
#             form1.save()
#         else:
#             print('ERROR')
#     return render(request,'doctorsapp/updateavai.html',{'form1':form1}) 


# class DoctorAvailability(ListView):
#     pass

from django.http import HttpResponseRedirect
class UpdateAvailability(UpdateView):
    model =Availabity
    form_class=AvaiForm
    success_url='/doctorsapp/addavailability'
    template_name='doctorsapp/updateavai.html'

    def form_valid(self, form):
      messages.success(self.request, "Detail updated sucessfully.")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())