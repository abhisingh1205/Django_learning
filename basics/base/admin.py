from django.contrib import admin
from .models import Student, School, Standard, Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'city', 'marks', 'pass_date']

admin.site.register(Standard)
admin.site.register(School)
admin.site.register(Teacher)

