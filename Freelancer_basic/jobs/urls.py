from django.urls import path
from .views import index, FreelancerListView, FreelancerDetailView

urlpatterns = [
    path('', FreelancerListView.as_view(), name='home'),
    path('developer/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),

]