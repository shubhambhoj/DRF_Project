from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('stud/',views.StudentList.as_view()),
    path('stud/',views.StudentCreate.as_view()),
    #path('stud/<int:pk>/',views.StudentRetrieve.as_view()),
    #path('stud/<int:pk>/',views.StudentUpdate.as_view()),
    #path('stud/<int:pk>/',views.StudentDestroy.as_view()),

    #path('stud/',views.StudentListCreate.as_view()),
    #path('stud/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    #path('stud/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    path('stud/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),

]
