from django.shortcuts import render

# Генерация стандартного HTTP ответа
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

# Create your views here.
