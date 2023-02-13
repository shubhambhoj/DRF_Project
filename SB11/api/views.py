from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_api(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            stu=Student.objects.get(id=pk)
            ser=StudentSerializer(stu)
            return Response(ser.data)
        stu=Student.objects.all()
        ser=StudentSerializer(stu, many=True)
        return Response(ser.data)

    elif request.method=="POST":
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Inserted Successfully!!!!"},status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="PUT":
        stu=Student.objects.get(id=pk)
        ser=StudentSerializer(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Completed Updated!!!"})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="PATCH":
        stu=Student.objects.get(id=pk)
        ser=StudentSerializer(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Partially Updated "})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({"msg":"Data Deleted Successfully"})
        