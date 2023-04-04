from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def division(request):
    return HttpResponse('''<h1>Division</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')

def subtraction(request):
    return HttpResponse('''<h1>Subtraction</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')

def addition(request):
    return HttpResponse('''<h1>Addition</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')

def multiplication(request):
    return HttpResponse('''<h1>Multiplies</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')
