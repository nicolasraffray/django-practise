from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Function for handling certain routes
def home(request):
  return HttpResponse('<h1> Home! </h1>')