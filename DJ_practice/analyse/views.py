from django.shortcuts import render
from django.http import HttpResponse
from .models import Explore
# Create your views here.

def index(req):
    # ex1 = Explore()
    # ex1.title = "Hyderabad"
    # ex1.rating = "20 ratings"
    # ex1.range = "10$ - 50$"
    # ex1.ex_type = "City"
    # ex1.img = "e1.jpg"
    # ex1.review = "Featured"
    # ex1.offer = True
    # ex1.description = "The is for biriyani lovers..."

    # ex2 = Explore()
    # ex2.title = "Bengalore"
    # ex2.rating = "13 ratings"
    # ex2.range = "50$ - 300$"
    # ex2.ex_type = "Bueatiful"
    # ex2.img = "e2.jpg"
    # ex2.offer = True
    # ex2.review = "Best rated"
    # ex2.description = "The city of beautiful weather.."

    # ex3 = Explore()
    # ex3.title = "Chennai"
    # ex3.rating = "19 ratings"
    # ex3.range = "15$ - 30$"
    # ex3.ex_type = "Kochadian"
    # ex3.img = "e3.jpg"
    # ex3.review = "More Viewed"
    # ex3.offer = True
    # ex3.description = "The cultural city we can ever think of."

    # ex4 = Explore()
    # ex4.title = "Mumbai"
    # ex4.rating = "19 ratings"
    # ex4.range = "15$ - 30$"
    # ex4.ex_type = "Stocks"
    # ex4.img = "e4.jpg"
    # ex4.description = "The city of gold and guns."

    # ex5 = Explore()
    # ex5.title = "Mumbai"
    # ex5.rating = "19 ratings"
    # ex5.range = "15$ - 30$"
    # ex5.ex_type = "Stocks"
    # ex5.img = "e5.jpg"
    # ex5.description = "The city of gold and guns."

    # ex6 = Explore()
    # ex6.title = "Mumbai"
    # ex6.rating = "19 ratings"
    # ex6.range = "15$ - 30$"
    # ex6.ex_type = "Stocks"
    # ex6.img = "e6.jpg"
    # ex6.description = "The city of gold and guns."

    # explores = [ex1, ex2, ex3]

    explores = Explore.objects.all()
    return render(req, 'index.html', {"explores":explores})