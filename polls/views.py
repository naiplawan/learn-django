from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

## write function to return request object to the browser
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")