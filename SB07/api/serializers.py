from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)            # for single fields
    class Meta:
        model=Student
        fields=['name','roll','city']
        #read_only_fields=['name', 'roll']                   # for multiple fields
        extra_kwargs={'name':{'read_only':True}}