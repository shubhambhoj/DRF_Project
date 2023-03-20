from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly



@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])

def student_api(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            stu=Student.objects.get(id=pk)
            ser=StudentSerializer(stu)
            return Response(ser.data)
        stu=Student.objects.all()
        ser=StudentSerializer(stu, many=True)
        return Response(ser.data)

    if request.method=='POST':
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Inserted Successfully!!!"})
        return Response(ser.errors)

    if request.method=='PUT':
        stu=Student.objects.get(id=pk)
        ser=StudentSerializer(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Updated completly!!!"})
        return Response(ser.errors)

    if request.method=='PATCH':
        stu=Student.objects.get(id=pk)
        ser=StudentSerializer(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data Updated Partially!!!"})
        return Response(ser.errors)

    if request.method=='DELETE':
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({"msg":"Data Deleted Successfully!!!!"})