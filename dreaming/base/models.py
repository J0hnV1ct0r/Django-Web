from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    kind = models.CharField(max_length=100, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['kind']


class Challenge(models.Model):
    book = models.ForeignKey(Work, related_name='challenges', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']


class Review(models.Model):
    work = models.ForeignKey(Work, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])  # ver como adicionar limite superior e inferior

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['score']


class Journal(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='journals', on_delete=models.CASCADE)
    entry_name = models.CharField(max_length=200, null=True)
    entry = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
