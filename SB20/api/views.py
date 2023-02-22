from django.shortcuts import render
from rest_framework import viewsets
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    #permission_classes=[AllowAny]
    #permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]