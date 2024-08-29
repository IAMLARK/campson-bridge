from django.urls import path
from . import views

urlpatterns = [
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('course_management/', views.course_management, name='course_management'),
    path('add_course', views.add_course, name='add_course'),
    path('course_details/<int:pk>', views.course_details, name='course_details'),
    path('total_user/', views.total_user, name='total_user'),
    path('update_course/<int:pk>', views.update_course, name='update_course'),
    path('delete_course/<int:pk>', views.delete_course, name='delete_course'),

]
