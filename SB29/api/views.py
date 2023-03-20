from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
#from rest_framework.authentication import SessionAuthentication
from api.auth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]    

