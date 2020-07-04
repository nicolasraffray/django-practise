from django.shortcuts import render

# Create your views here.

# Function for handling certain routes
def home(request):
  return render(request, 'blog/home.html')

def about(request):
  return render(request, 'blog/about.html')