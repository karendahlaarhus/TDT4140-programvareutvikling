from django.urls import reverse
from django.db import models
from django import forms

class Vaskeliste(models.Model):

    class Meta:
        verbose_name_plural = "Vaskelister"

class Task(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    vaskeliste = models.ForeignKey(Vaskeliste(), on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.text


