from django.shortcuts import render
from django.http import HttpResponse
from .models import Explore
# Create your views here.

def index(req):
    ex1 = Explore()
    ex1.title = "Taj Mahal"
    ex1.rating = "23 ratings"
    ex1.range = "10$ - 50$"
    ex1.ex_type = "Wonder"
    ex1.description = "The 7 wonder of the world which is nothing but a taj mahal from india...."
    return render(req, 'index.html', {"ex1":ex1})