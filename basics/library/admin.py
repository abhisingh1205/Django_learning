from django.contrib import admin
from .models import LB_User, Author, Books, Publisher, Employee
# Register your models here.

admin.site.register(LB_User)

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(Employee)
