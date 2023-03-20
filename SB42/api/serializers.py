from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        #fields=['id','url','name','roll','city']
        fields='__all__'