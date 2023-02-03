from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            ser=StudentSerializer(stu)
            # json_data=JSONRenderer().render(ser.data)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(ser.data,safe=True)

        stu=Student.objects.all()
        ser=StudentSerializer(stu,many=True)
        # json_data=JSONRenderer().render(ser.data) 
        # return HttpResponse(json_data,content_type='application/json') 
        return JsonResponse(ser.data,safe=False)  

    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        ser=StudentSerializer(data=pythondata)
        if ser.is_valid():
            ser.save()
            res={'msg':"Data Successfully Inserted"}
            # json_data=JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res,safe=False) 
        
        # json_data=JSONRenderer().render(ser.errors)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(ser.errors,safe=False) 
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        # PARTIAL UPDATE-ALL DATA NOT REQUIRED
        ser=StudentSerializer(stu,data=pythondata,partial=True)
        # COMPLETE UPDATE-  ALL DATA REQUIRED FROM FRONT END / CLIENT
        #ser=StudentSerializer(stu,data=pythondata)
        if ser.is_valid():
            ser.save()
            res={'msg':'Student Update Successfully'}
            # json_data=JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type="application/json")
            return JsonResponse(res,safe=False) 

        # json_data=JSONRenderer().render(ser.errors)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(ser.errors,safe=False) 
        
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Student Delete Successfully'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(res,safe=False) 


