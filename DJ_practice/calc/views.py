from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = render(request, 'home.html', {'name': 'Eswar'})
    return response

def add(req):
    n1 = int(req.POST['num1'])
    n2 = int(req.POST['num2'])
    res = n1 + n2
    return render(req, 'result.html', {'answer': res})