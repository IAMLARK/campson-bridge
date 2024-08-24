from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages

# Create your views here.
def student_dashboard(request):
    return render(request, "student_dashboard.html", {})


def login_user(request):
  if request.method == "POST" :

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, ("You have been logged in"))
        return redirect('student_dashboard')
    else:
        messages.success(request, ("There was a problem logging in"))
        return redirect('login')

  else:
    return render(request, 'student_dashboard.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')


         
