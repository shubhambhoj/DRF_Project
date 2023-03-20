from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


# CRUD OPERATIONS WITH TOKEN AUTHENTICATION:
'''
GET request: list of all data
http GET http://127.0.0.1:8000/studentapi/ "Authorization:Token 53f141b929b28d4065caf6dcf554286e7d90c47c"


GET request: single record
http GET http://127.0.0.1:8000/studentapi/2/ "Authorization:Token 53f141b929b28d4065caf6dcf554286e7d90c47c"

POST request: Insert Record
http POST http://127.0.0.1:8000/studentapi/ name=jay roll=104 city=pune  "Authorization:Token 53f141b929b28d4065caf6dcf554286e7d90c47c"

PUT request: Complete Update
http PUT http://127.0.0.1:8000/studentapi/4/ name=vijay roll=104 city=mumbai  "Authorization:Token 53f141b929b28d4065caf6dcf554286e7d90c47c"

PATCH request: Partial update
http PATCH http://127.0.0.1:8000/studentapi/4/ name=sanjay  city=phaltan  "Authorization:Token 53f141b929b28d4065caf6dcf554286e7d90c47c"

DELETE request : Delete Record
http DELETE http://127.0.0.1:8000/studentapi/5/ "Authorization:Token 53f141b929b28d4065caf6dcf554286e7d90c47c"
'''