
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

#1) Model Object - Single Student Data
#   1)WITHOUT JsonResponse
'''
def student_detail(request):
    stu=Student.objects.get(id= 1)
    ser=StudentSerializer(stu)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')
'''
#   1)WITH JsonResponse
'''
def student_detail(request):
    stu=Student.objects.get(id= 2)
    ser=StudentSerializer(stu)
    return JsonResponse(ser.data, safe=True)
'''
#   1)Dynamic way
def student_detail(request,pk):
    stu=Student.objects.get(id= pk)
    ser=StudentSerializer(stu)
    return JsonResponse(ser.data, safe=True)


#2) Model Object - All Student Data
#   1)WITHOUT JsonResponse
'''
def student_list(request):
    stud=Student.objects.all()
    ser=StudentSerializer(stud,many=True)
    json_list=JSONRenderer().render(ser.data)
    return HttpResponse(json_list,content_type='application/json')
'''
#   1)WITH JsonResponse
def student_list(request):
    stud=Student.objects.all()
    ser=StudentSerializer(stud,many=True)
    #return JsonResponse(ser.data,safe=True)
    return JsonResponse(ser.data,safe=False)