
from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls')),
    path('stud/',views.StudentList.as_view())
    
]
