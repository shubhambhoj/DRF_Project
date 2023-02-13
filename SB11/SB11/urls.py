
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud/', views.student_api),
    path('stud/<int:pk>/', views.student_api),
]
