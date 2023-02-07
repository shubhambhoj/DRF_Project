from rest_framework import serializers
from api.models import Student
#  Validators :
def start_with_r(value):
    if value[0]!='r':
        raise serializers.ValidationError("Name should Start with 'r'")

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100, validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.roll=validated_data.get('roll', instance.roll)
        instance.city=validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field Level Validation :
    def validate_roll(self, values):
        if values >=150:
            raise serializers.ValidationError("Seats are Full")
        return values

    # Object Level Validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='ram' and ct.lower()!='pune':
            raise serializers.ValidationError("city must be pune ")
        return data 

            