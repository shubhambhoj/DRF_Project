from django.shortcuts import render
from api.models import Student,Teacher
from api.serializers import StudentSerializer,TeacherSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import CustomUserRateThrottle

class StudentAPIView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle, UserRateThrottle]

class TeacherAPIView(ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle, CustomUserRateThrottle ]