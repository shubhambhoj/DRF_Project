from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

class StudentAPIView(APIView):
    def get(self,request,pk=None, format=None):
        if  pk is not None:
            stu=Student.objects.get(id=pk)
            ser=StudentSerializer(stu)
            return Response(ser.data)
        stu=Student.objects.all()
        ser=StudentSerializer(stu,many=True)
        return Response(ser.data)

    def post(self,request,format=None):
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data inserted Successfully!!!!"},status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        stu=Student.objects.get(id=pk)
        ser=StudentSerializer(stu,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Data updated completelly!!!"})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        stu=Student.objects.get(id=pk)
        ser=StudentSerializer(stu,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"data updated partially!!!"})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({"msg":"Data Deleted Successfully!!!"})