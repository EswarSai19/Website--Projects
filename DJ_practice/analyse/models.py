from django.db import models

# Create your models here.
# class Explore:
#     id: int
#     title: str
#     rating: str
#     ex_type: str
#     description: str
#     review : str
#     offer : bool


class Explore(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    rating = models.CharField(max_length=30)
    ex_type = models.CharField(max_length=30)
    description = models.TextField()
    pr_range = models.CharField(max_length=30)
    review = models.CharField(max_length=30)
    offer = models.BooleanField(default=False)  # Corrected