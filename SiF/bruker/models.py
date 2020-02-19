from django.db import models

# Create your models here.

class bruker(models.Model):
    brukernavn = models.CharField(max_length=30)
    isManager = models.BooleanField()
    kollektiv = models.ForeignKey(kollektiv)


