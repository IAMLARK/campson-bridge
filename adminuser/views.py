from django.shortcuts import render, redirect
from .models import Course
from .forms import AddCourseForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# no of users in system
def total_user(request):
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    all_users = User.objects.all()
    return render(request, "total_user.html", {'total_users': total_users, 'active_users':active_users, 'all_users':all_users})

def admin_dashboard(request):
    return render(request, "admin_dashboard.html", {})

def course_management(request): 
    courses = Course.objects.all()
    return render(request, "course_management.html", {'courses':courses})

def course_details(request, pk):
    # if request.user.is_authenticated:
        # look up for records
        course_details = Course.objects.get(id=pk)
        return render(request, 'course_details.html', {'course_details':course_details})
    # else:
    #     messages.success(request, "You must be logged in to view that page..")
    #     return redirect('home')

def add_course(request):
    form = AddCourseForm(request.POST or None)
    # if request.user.is_authenticated:
    if request.method == "POST":
            if form.is_valid():
                add_course = form.save()
                messages.success(request, "Record Added..")
                return redirect('course_management')
       
    return render(request, 'add_course.html', {'form':form})
    # else:
    #     # messages.success(request, "You must be logged in..")   
    #     return redirect('home')
    
def update_course(request, pk):
    # if request.user.is_authenticated:
        current_record = Course.objects.get(id=pk)
        form =  AddCourseForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated..")
            return redirect('course_management')
        return render(request, 'update_course.html', {'form':form})
    # else:
    #      messages.success(request, "You must be logged in..")   
    #      return redirect('home')
    
def delete_course(request, pk):
    # if request.user.is_authenticated:
        delete_it = Course.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully..")
        return redirect('course_management')
    # else:
    #     messages.success(request, "You must be logged in to do that..")
    #     return redirect('home')   
    





