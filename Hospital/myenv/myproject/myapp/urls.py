
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('patientregistration',views.patientregistration,name='patientregistration'),
    path('patientappointment',views.patientappointment,name='patientappointment'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('UserModule', views.UserModule, name='UserModule'),
    path('viewappointment', views.viewappointment, name='viewappointment'),
    path('viewp', views.viewp, name='viewp'),
    path('doctor', views.doctor, name='doctor'),
    path('contact', views.contact, name='contact'),  
    path('DoctorModule', views.DoctorModule, name='DoctorModule'),  
    path('doctorregistration',views.doctorregistration,name='doctorregistration'),
    path('approveappointment', views.approveappointment, name='approveappointment'),
    path('base', views.base, name='base'),

]
