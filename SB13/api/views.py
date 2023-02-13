from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView

# ListModelMixin 
class StudentListAPI(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

# CreateModelMixin
class StudentCreateAPI(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

# RetrieveModelMixin
class StudentRetrieveAPI(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

# UpdateModelMixin
class StudentUpdateAPI(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDeleteAPI(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)