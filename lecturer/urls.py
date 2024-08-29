from django.urls import path
from . import views

urlpatterns = [
    
    path('lecturer_dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    

]
