from django.shortcuts import render

#def home(request):
  #  return render(request)

from django.http import HttpResponse

def homepage(request):
    return render(request,"home.html")

def aboutUS(request):
    return HttpResponse("Welcome!")
def home(request):
    return HttpResponse("homepage")

def contact(request):
    return HttpResponse("Contact Us!")