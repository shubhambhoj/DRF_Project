from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stud/',views.StudentListCreate.as_view()),
    path('stud/<int:pk>/',views.StudentRetUpdDest.as_view()),
]
