from django.db import models
from django.conf import settings


class Person(models.Model):
    name = models.CharField(max_length=255)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    geo_location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    people = models.ManyToManyField(Person, related_name='images', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
