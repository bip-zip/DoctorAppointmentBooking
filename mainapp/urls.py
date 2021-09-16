from django.urls import path
from mainapp import views
 

urlpatterns=[
    path('home',views.home, name='home'), 
    path('about',views.about, name='about'),
    path('profile',views.profile, name='profile'),
    path('contact',views.contact, name='contact'),
    path('appointment',views.appointment, name='appointment'),
    path('oldappointment',views.oldappointment, name='oldappointment'),
    path('response/<int:id>',views.response, name='response'),



    path('checkAvaibility',views.checkAvaibility, name='checkAvaibility'),


]


