from django.shortcuts import render
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("***************LIST**********************")
        print("Basename: ",self.basename)
        print("Action: ",self.action)
        print("Detail: ",self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)

        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        print("***************RETRIEVE**********************")
        print("Basename: ",self.basename)
        print("Action: ",self.action)
        print("Detail: ",self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)

        if pk is not None:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("***************CREATE**********************")
        print("Basename: ",self.basename)
        print("Action: ",self.action)
        print("Detail: ",self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)

        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Inserted"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("***************UPDATE**********************")
        print("Basename: ",self.basename)
        print("Action: ",self.action)
        print("Detail: ",self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)

        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Completely Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        print("***************PARTIAL UPDATE**********************")
        print("Basename: ",self.basename)
        print("Action: ",self.action)
        print("Detail: ",self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)

        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Partially Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request, pk):
        print("***************DESTROY**********************")
        print("Basename: ",self.basename)
        print("Action: ",self.action)
        print("Detail: ",self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({"msg":"Data Deleted Successfully!!!"})

