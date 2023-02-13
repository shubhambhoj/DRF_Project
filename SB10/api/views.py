from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if  request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            ser=StudentSerializer(stu)
            return Response(ser.data)
        stu=Student.objects.all()
        ser=StudentSerializer(stu, many=True)
        return Response(ser.data)

    elif request.method =='POST':
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'data created successfully'})
        return Response(ser.errors)

    elif request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        ser=StudentSerializer(stu,data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'data updated successfully!!'})
        return Response(ser.errors)
    
    elif request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted successfully!!'})