from django.db import models
from django.db.models.query import QuerySet

class StudentsManager(models.Manager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().order_by('name')
    
    def get_above_marks_range(self, m1, m2):
        return super().get_queryset().filter(marks__range=(m1, m2)) 