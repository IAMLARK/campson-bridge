from django.urls import path
from . import views

urlpatterns = [
    
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
   

]
