from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    teacher_id=models.IntegerField()
    city=models.CharField(max_length=100)