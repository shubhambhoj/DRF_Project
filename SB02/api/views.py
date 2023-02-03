from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data=request.body
        print("request.body:",request.body)
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        ser=StudentSerializer(data=pythondata)
        if ser.is_valid():
            ser.save()
            res={'msg':'data inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(ser.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=="GET":
        stu=Student.objects.all()
        ser=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(data)        

        

