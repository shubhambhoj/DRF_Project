from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud/',views.StudentListAPI.as_view()),
    #path('stud/',views.StudentCreateAPI.as_view()),
    #path('stud/<int:pk>/',views.StudentRetrieveAPI.as_view()),
    #path('stud/<int:pk>/',views.StudentUpdateAPI.as_view()),
    path('stud/<int:pk>/',views.StudentDeleteAPI.as_view()),
]
