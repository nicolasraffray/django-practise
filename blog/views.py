from django.shortcuts import render

# Posts

posts = [ 
  {
    'author' : 'Nic',
    'title' : 'Blog Post 1',
    'content' : 'first post content',
    'data': '4 July, 2020'
  },
  {
    'author' : 'Jane',
    'title' : 'Blog Post 2',
    'content' : 'second post content',
    'data': '5 July, 2020'
  }

]

# Create your views here.

# Function for handling certain routes
def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')