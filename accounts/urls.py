from django.urls import path
from accounts import views
from .views import ProfileUpdateView,DoctorProfileUpdateView

urlpatterns=[
    path('',views.login_user, name='login'),
    path('register',views.register_user, name='register'),
    path('registerdoctor',views.register_doctor, name='register_doctor'),
    path('update/<pk>', ProfileUpdateView.as_view(), name='profileupdate'), 
    path('updatedoctor/<pk>', DoctorProfileUpdateView.as_view(), name='dprofileupdate'), 
    path('logout',views.logout_user, name='logout'),
]




