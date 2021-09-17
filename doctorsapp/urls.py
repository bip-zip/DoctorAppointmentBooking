from django.urls import path
from . import views
from .views import AddAvaibality,UpdateAvailability

urlpatterns =[
    path('',views.doctor_home,name="doctorhome"),
    path('allappointments',views.allAppointments,name="allAppointments"),
    path('deleteava/<int:id>',views.deleteAvailability,name="deleteAvailability"),
    path('addavailability',AddAvaibality.as_view(),name="addavai"),
    path('update-avai/<pk>',UpdateAvailability.as_view(),name="updateavai"),
    path('appdetail/<int:id>',views.appdetail, name='appdetail'),

    
]