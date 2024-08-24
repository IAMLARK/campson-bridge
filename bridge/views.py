from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def portal(request):
    return render(request, 'portal.html', {})








