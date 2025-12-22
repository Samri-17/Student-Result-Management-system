from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login #authentiace is a predefined function in django to check user credentials
from django.contrib import messages
# Create your views here.
def index(request):
    """
    index.html page created in template is called
    home page kholna ko lagi
    """
    return render(request,'index.html') 

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard') # if user is already logged in, redirect to admin home page
    error=None
    if request.method == 'POST':
        username=request.POST['username'] # get username from form
        password=request.POST['password']   
        user = authenticate(request, username=username, password=password) # check if username and password are correct
        if user is not None and user.is_superuser: # check if user exists and is superuser 
            login(request, user)
            return redirect('admin_dashboard') # if login is successful, redirect to admin home page
        else:
            error="Invalid username or password" # if login fails, show error message


    """
    admin_login.html page created in template called
    admin login page kholna ko lagi
    """
    return render(request,'admin_login.html',locals())

def admin_dashboard(request):
    """
    admin_dashboard.html page created in template called
    admin home page kholna ko lagi
    """
    return render(request,'admin_dashboard.html')