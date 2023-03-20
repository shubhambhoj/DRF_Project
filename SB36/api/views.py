from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    #ordering_fields=['name']
    #ordering_fields=['name','city']
    ordering_fields='__all__'
    
    
