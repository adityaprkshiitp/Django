from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1><center>HOME</center></h1><br><a href="http://127.0.0.1:8000/division"> <b>Divide here</b></a>
    <br><a href="http://127.0.0.1:8000/subtraction"> <b>Subtract here</b></a>
    <br><a href="http://127.0.0.1:8000/addition"> <b>Add here</b></a>
    <br><a href="http://127.0.0.1:8000/multiplication"> <b>Multiply here</b></a>''')

def division(request):
    return HttpResponse('''<h1>Division</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')

def subtraction(request):
    return HttpResponse('''<h1>Subtraction</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')

def addition(request):
    return HttpResponse('''<h1>Addition</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')

def multiplication(request):
    return HttpResponse('''<h1>Multiplies</h1> <a href="http://127.0.0.1:8000"> Go back to Homepage</a>''')
