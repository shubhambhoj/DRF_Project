from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # validator
    def starts_with_r(value):
        if value[0]!='r':
            raise serializers.ValidationError('Name should Starts with r')

    name=serializers.CharField(max_length=100,validators=[starts_with_r]) 
    
    class Meta:
        model=Student
        fields=['name','roll','city']
    
    # field level validation
    def validate_roll(self, value):
        if value >=200:
            raise serializers.ValidationError('Seats are full')
        return value

    # object level validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if  nm.lower()=='ram' and ct.lower()!='pune':
            raise serializers.ValidationError('city must be pune')
        return data