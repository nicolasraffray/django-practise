from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Function for handling certain routes
def home(request):
  return render(request, 'blog/home.html')

def about(request):
  return HttpResponse('<h1> About Page </h1>')