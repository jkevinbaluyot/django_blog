from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the blog home page!</h1>")

def about(request):
    return HttpResponse("<h1>About the blog</h1><p>This is a simple blog application.</p>")