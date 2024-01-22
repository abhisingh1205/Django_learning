from .models import Student, Standard, Teacher
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
    
class StandardSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    student = StudentSerializer(many=True)
    
    class Meta:
        model = Standard
        fields = '__all__'