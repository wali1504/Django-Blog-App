from django.urls import path
from . import views
#from theblog import views

urlpatterns = [
    path('', views.homepage),
    path('home/', views.home), 
    path('about-us/', views.aboutUS),
    path('contact/', views.contact),
]