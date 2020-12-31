from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'you are successfully loged in')
            return redirect('home')
        else:
            messages.warning(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'home/login.html')
    
def home(request):
    return render(request,'home/index.html')

def logout(request):
    auth.logout(request)
    messages.success(request,'you are successfully loged out')
    return redirect('/')    