from django.db.models import ProtectedError 
from django.shortcuts import render 



class GlobalExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response 
    
    def __call__(self,request):
        try:
            response = self.get_response(request)
            return response 
        except ProtectedError:
            message = "This category cannot deleted because it has related products."
            return render(request,"exercise/error.html",{'error':message})
        except Exception as e:
            return render(request,"exercise/error.html",{"error":str(e)})
