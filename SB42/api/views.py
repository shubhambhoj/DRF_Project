from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet

class StudentView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
