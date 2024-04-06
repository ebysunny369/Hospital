from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from.models import Patient,Appointment,Login,Doctor
from .forms import PatientForm,AppointmentForm,LoginForm,DoctorForm
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def doctor(request):
    return render(request,'doctor.html')
def contact(request):
    return render(request,'contact.html')    


def patientappointment(request):
    if request.method=="POST":
            form=AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'home.html')
    else:
        form=AppointmentForm()
    return render(request,'patientappointment.html')


def patientregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1: 
            if User.objects.filter(username=username).exists():
                #messages.info(request,"username taken")
                return redirect('patientregistration')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            #print("user created")
        else:
            #print("password not matched")
            return redirect('patientregistration')
        return redirect('/')

    else:
        return render(request,'patientregistration.html')

def doctorregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1: 
            if User.objects.filter(username=username).exists():
                #messages.info(request,"username taken")
                return redirect('doctorregistration')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            #print("user created")
        else:
            #print("password not matched")
            return redirect('doctorregistration')
        return redirect('/')

    else:
        return render(request,'doctorregistration.html')    

def UserModule(request):
    return render(request,'UserModule.html')
def viewappointment(request):
    return render(request,'viewappointment.html')
def DoctorModule(request):
    return render(request,'DoctorModule.html')
def viewp(request):
    return render(request,'viewp.html')
def approveappointment(request):
    return render(request,'approveappointment.html')
def base(request):
    return render(request,'base.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username, password=password)
            if user is not None:
                print(user)
                return render(request, 'UserModule.html')
            return render(request, 'login.html')
        except:
            pass
        try:
            user = Login.objects.get(username=username, password=password)
            if user is not None:
                print(user)
                return render(request, 'home.html')
                # return render(request,'Adminmodule.html')
        except:
            pass
        try:
            user = Doctor.objects.get(username=username, password=password)
            if user is not None:
                print(user)
                return render(request, 'DoctorModule.html')
            return render(request, 'login.html')
        except:
            pass
    else:
        return render(request, 'login.html')




