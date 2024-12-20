from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from jobs.models import Freelancer, Business
def index(request):
    # return render(request, 'index.html')
    return HttpResponse('<h1>Hello, World! I am a freelancer</h1>')

class FreelancerListView(ListView):
    model = Freelancer

class FreelancerDetailView(DetailView):
    model = Freelancer
    