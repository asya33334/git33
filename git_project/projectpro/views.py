from django.shortcuts import render

# Генерация стандартного HTTP ответа
from django.http import HttpResponse

#def index(request):
    #return HttpResponse("Hello, World!")

# Create your views here.
def index(request):
    print(request.__dict__)
    return render(request, 'projectpro/index.html')

def about(request):
    return render(request, 'projectpro/index2.html')