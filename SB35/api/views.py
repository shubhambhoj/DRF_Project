from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    #search_fields=['city']                 # SINGLE FIELD SEARCH
    #search_fields=['name','city            # MULTIPLE FIELDS SEARCH
    #search_fields=['^name']                # START WITH
    #search_fields=['=name']                # EXACT MATCHES
    #search_fields=['@city']                #FULL-TEXT SEARCH(currently only support Django's postgresSQL)
    search_fields=['$city']                 # REGEX SEARCH

