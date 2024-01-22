from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    print("Inside Home View")
    return HttpResponse("This is Home View")