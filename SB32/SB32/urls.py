from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls')),
    path('stud/',views.StudentListAPIView.as_view()),
    #path('stud/',views.StudentCreateAPIView.as_view()),
    #path('stud/<int:pk>/',views.StudentRetrieveAPIView.as_view()),
    path('stud/<int:pk>/',views.StudentUpdateAPIView.as_view()),
    #path('stud/<int:pk>/',views.StudentDestroyAPIView.as_view()),
]
