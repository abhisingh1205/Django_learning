from typing import Any
from django.shortcuts import render
from django.db.models import Avg
from .models import Student, School, Standard, Teacher
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .serializers import StudentSerializer, StandardSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.status import *
import xmltodict

# Create your views here.


def home(request):
    students_all = Student.students.all().order_by('id')
    paginator = Paginator(students_all, per_page=4)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    #print("Student data\n", students_all)
    #print("SQL Query\n", students_all.query)
    print("Paginator = ", paginator)
    print("page_no = ", page_no)
    print("Page obj  = ", page_obj)
    return render(request, 'base/home.html', {'students': page_obj})

def profile(request, roll_no):
    student = Student.students.get(roll_no=roll_no)
    return render(request, 'base/profile.html', {'student': student})

def cityaverage(request):
    city_avg = Student.students.values('city').annotate(total_sum=Avg('marks'))
    print("City average = ", city_avg)
    return render(request, 'base/city.html', {'citys': city_avg})


class HomeListView(ListView):
    model = Student
    template_name = 'base/home.html'
    ordering = ['id']
    paginate_by = 4
    paginate_orphans = 1

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            return super(HomeListView, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(HomeListView, self).get_context_data(**kwargs)
        

def get_all_students(request):
    students = Student.students.get_above_marks_range(95, 100)

    return render(request, 'base/home.html', {'students': students})

class StudentJSONView(APIView):

    def get(self, request, *args, **kwargs):
        my_students = Student.students.all()
        serializer = StudentSerializer(my_students, many=True)
        print(serializer.data)
        #Response function converts the Python dict to JSON automatically or we can use JSONRenderer
        #return Response(serializer.data)
        #json_data = JSONRenderer().render(serializer.data)

        return JsonResponse(serializer.data, safe=False)
    
class StudentXMLView(APIView):
    def get(self, request, *args, **kwargs):
        my_student = Student.students.all()
        serializer = StudentSerializer(my_student, many=True)
        xml_data = {'data': serializer.data}
        my_data = xmltodict.unparse({'data': xml_data}, pretty=True)
        print("My data = ", my_data)
        return HttpResponse(my_data, content_type="application/xml")
    

class StandardView(APIView):
    def get(self, request, *args, **kwargs):
        standard_data = Standard.objects.all()
        print("Standard Queryset = ", Standard.objects.all().values('student__id'))
        #students = standard_data.student
        #print("Student = ", students)
        
        for stu in Standard.objects.all().values('student__id'):
            student = Student.objects.get(id=stu['student__id'])

        #standards = Standard.objects.select_related('school').all()
        #print(str(standards))
        standards = Standard.objects.prefetch_related('student').all()
        for standard in standards:
            #school_obj = standard.school
            #print("School =", school_obj)

            student_obj = standard.student
            print("Student = ", student_obj)
        
        serializer = StandardSerializer(standard_data, many=True)

        return Response({'data': serializer.data}, status=HTTP_200_OK)
    

        