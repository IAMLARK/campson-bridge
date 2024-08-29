
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bridge.urls")),
    path('', include("student.urls")),
    path('', include("lecturer.urls")),
    path('', include("adminuser.urls")),
    
]
