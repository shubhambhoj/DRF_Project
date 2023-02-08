from django.shortcuts import render
from django.views import View
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            ser=StudentSerializer(stu)
            return JsonResponse(ser.data, safe=True)
        stu=Student.objects.all()
        ser=StudentSerializer(stu, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(salf,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        ser=StudentSerializer(data=pythondata)
        if ser.is_valid():
            ser.save()
            res={'msg':'data inserted successfully'}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)
        
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        ser=StudentSerializer(stu, data=pythondata)
        if ser.is_valid():
            ser.save()
            res={'msg':'data updated successfully!!!'}
            return JsonResponse(res, safe=False)
        return JsonResponse(ser.errors, safe=False)

    def delete(self, request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted successfully'}
        return JsonResponse(res, safe=False)