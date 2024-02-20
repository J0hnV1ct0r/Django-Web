from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    kind = models.CharField(max_length=100, blank=True)
    image = models.ImageField()


class Challenge(models.Model):
    book = models.ForeignKey(Work, related_name='challenges', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    work = models.ForeignKey(Work, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True) #ver como adicionar limite superior e inferior
