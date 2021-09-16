from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm,UserCreationForm,ProfileForm,DoctorForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import AppUser, DoctorUser

def register_user(request):
    if request.method == "POST":
        user_form=UserCreationForm(request.POST)
        signup_form=ProfileForm(request.POST,request.FILES)

        if user_form.is_valid() and signup_form.is_valid():
            user=user_form.save(commit=False)
            email=user.email
            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR, 'Email already registered!!')
                return HttpResponseRedirect(reverse('accounts:register'))
            
            user.save()
            profile = signup_form.save(commit=False)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.user_id=user.id
            profile.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully!')
            return HttpResponseRedirect(reverse('accounts:login'))
            
        else:
           
            messages.add_message(request, messages.ERROR,
                                 'Error in registering user')
            return render(request, 'mainapp/register.html', {'form1': user_form, 'form2':signup_form})
    context = {
        'form1': UserCreationForm(), 
        'form2':ProfileForm(),
        'active_register':'active'
    }
    return render(request,'mainapp/register.html',context)
  



def logout_user(request):
    logout(request)
    return redirect('/')




def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active and user.is_staff and user.is_superuser:
                    login(request, user)
                    return redirect('/admin')
                
                elif user.is_staff and user.is_active:
                    login(request, user)
                    return redirect('doctorsapp:doctorhome')
                else: 
                    login(request, user)
                    return redirect('mainapp:home')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Invalid username or password')
                return render(request, 'mainapp/login.html', {'form':form})
    context = {
        'form': LoginForm,
        'active_login':'active'
    }
    return render(request,'mainapp/login.html',context)


from django.views.generic.edit import UpdateView
class ProfileUpdateView(UpdateView):
    model = AppUser
    fields = ['profile_pic','age', 'contact','address']
    success_url =("/app/profile")

    def form_valid(self, form):
      messages.success(self.request, "Details updated successfully!")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())


def register_doctor(request):
    if request.method == "POST":
        user_form=UserCreationForm(request.POST)
        signup_form=DoctorForm(request.POST,request.FILES)

        if user_form.is_valid() and signup_form.is_valid():
            user=user_form.save(commit=False)
            email=user.email
            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.ERROR, 'Email already registered!!')
                return HttpResponseRedirect(reverse('accounts:register'))
            user.is_active=False
            user.save()
            profile = signup_form.save(commit=False)
            
            profile.user_id=user.id
            profile.save()
            messages.add_message(request, messages.SUCCESS, "Completed registration but you'll get an email when our admin approve your details")
            return HttpResponseRedirect(reverse('accounts:login'))
            
        else:
           
            messages.add_message(request, messages.ERROR,
                                 'Error in registering user')
            return render(request, 'mainapp/register.html', {'form1': user_form, 'form2':signup_form})
    context = {
        'form1': UserCreationForm(), 
        'form2':DoctorForm(),
        'active_register':'active'
    }
    return render(request,'doctorsapp/doctorregister.html',context)

class DoctorProfileUpdateView(UpdateView):
    model = DoctorUser
    fields = '__all__'
    fields = ['profile_pic','contact', 'total_experience_years','address','specilization','maximum_degree']
    success_url =("/doctorsapp/")

    def form_valid(self, form):
      messages.success(self.request, "Details updated successfully!")
      super().form_valid(form)
      return HttpResponseRedirect(self.get_success_url())