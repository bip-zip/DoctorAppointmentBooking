from django.urls import path
from . import views
from .views import AddAvaibality,UpdateAvailability

urlpatterns =[
    path('',views.doctor_home,name="doctorhome"),
    path('addavailability',AddAvaibality.as_view(),name="addavai"),
    path('update-avai/<pk>',UpdateAvailability.as_view(),name="updateavai"),
    
]