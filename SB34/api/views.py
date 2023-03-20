from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend   

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # filterset_fields=['passby']
    # filterset_fields=['name','city']

    filter_backends=[DjangoFilterBackend]           # per View setting
    #filterset_fields=['passby']
    filterset_fields=['name','city']


    