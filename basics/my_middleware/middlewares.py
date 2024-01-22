from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import resolve, reverse


def custom_middleware(get_response):
    #print("One time initialization")

    def inner_function(request):
    #    print("This is before view")
        response = get_response(request)
    #    print("This is after view")
        return response
    
    return inner_function


class CustomClassMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Class one time initialization")

    def __call__(self, request):

        print("-----Class Based Middleware--------")
        print("This is before response cycle")
        response = self.get_response(request)
        print("This is after response cycle")
        return response
    
class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        self.count = self.count + 1
        #response = self.get_response(request)
        return HttpResponse(f"No of Refresh = {self.count}")
    

class CheckBadRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        current_url = request.path_info
        print("Current_Url = ", current_url)

        try:
            resolve_result = resolve(current_url)
            print("Result = ", resolve_result)
        except Exception as e:
            home_page_url = reverse('home')
            return HttpResponseRedirect(home_page_url)
        
        response = self.get_response(request)

        return response