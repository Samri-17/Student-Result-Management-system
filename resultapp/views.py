from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #authentiace is a predefined function in django to check user credentials
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
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
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_dashboard.html')

def admin_logout(request):  
    logout(request)
    return redirect('admin_login')

@login_required(login_url='admin_login')
def create_class(request):
    # if not request.user.is_authenticated:
    #     return redirect('admin_login')
    if request.method == 'POST':
        try:
            Year = request.POST.get('Year')
            Semester = request.POST.get('Semester')
            Class.objects.create(Year=Year, Semester=Semester)
            messages.success(request, "Class created successfully.")
            return redirect('create_class') # Redirect to the same page after successful creation
        except Exception as e:
            messages.error(request, f"Error creating class. Please try again. :{str(e)}")
    return render(request,'create_class.html')



from django.shortcuts import get_object_or_404
@login_required(login_url='admin_login')
def manage_class(request):
    classes=Class.objects.all()
    if request.GET.get('delete'):
        try:
            class_id=request.GET.get('delete')
            class_obj=get_object_or_404(Class, id=class_id)
            class_obj.delete()
            messages.success(request, "Class deleted successfully.")
            return redirect('manage_class')
        except Exception as e:
            messages.error(request, f"Error deleting class. Please try again. :{str(e)}")
            return redirect('manage_class')
    return render(request,'manage_class.html', locals())


@login_required(login_url='admin_login')
def edit_class(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id) # Get the class object or return 404 if not found
    if request.method == 'POST':
        try:
            Year = request.POST.get('Year')
            Semester = request.POST.get('Semester')
            class_obj.Year = Year  # Update the fields
            class_obj.Semester = Semester
            class_obj.save()  # Save the updated object
            messages.success(request, "Class updated successfully.")
            return redirect('manage_class') # Redirect to the same page after successful creation
        except Exception as e:
            messages.error(request, f"Error creating class. Please try again. :{str(e)}")
    return render(request,'edit_class.html', locals())