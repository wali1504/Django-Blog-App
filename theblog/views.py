#from django.shortcuts import render

#def home(request):
  #  return render(request)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
