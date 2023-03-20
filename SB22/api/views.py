from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAuthenticated
from api.custompermissions import MyCustomPermission

# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]
    permission_classes=[MyCustomPermission]