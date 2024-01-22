from django.db import models
from .managers import StudentsManager

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=255)
    roll_no = models.IntegerField(null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()

    #students = StudentsManager()

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Standard(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
