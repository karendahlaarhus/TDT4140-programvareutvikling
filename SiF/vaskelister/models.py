from django.urls import reverse
from django.db import models
from django import forms

from kollektiv.models import kollektiv


class Vaskeliste(models.Model):

    kollektiv = models.OneToOneField(kollektiv(), on_delete=models.CASCADE, null=True, blank=True) #kun et kollektiv til en vaskeliste
    def __str__(self):
        return str(self.kollektiv)
    class Meta:
        verbose_name_plural = "Vaskelister"

class Task(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    vaskeliste = models.ForeignKey(Vaskeliste(), on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.text


