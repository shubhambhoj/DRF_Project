from django.shortcuts import render
from rest_framework import viewsets
from api.models import Student
from api.serializers import StudentSerializer

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
