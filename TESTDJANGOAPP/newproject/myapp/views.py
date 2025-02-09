from django.shortcuts import render

# Create your views here.
from .models import Post
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
