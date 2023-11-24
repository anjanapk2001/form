from django.contrib import auth,messages
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse

from .forms import RegistrationForm, StudentForm
from .models import Course


# Create your views here.
def demo(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('success')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request, 'login.html')
def success(request):
    return render(request,'success.html')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html',{'form': form})





def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Add form processing logic here
            return render(request,'new.html')
    else:
        form = StudentForm()
    return render(request,'student_form.html',{'form': form})

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request,'course_dropdown_list.html',{'courses': courses})

def logout(request):
    auth.logout(request)
    return redirect('/')