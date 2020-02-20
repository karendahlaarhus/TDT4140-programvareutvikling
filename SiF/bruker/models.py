from django.db import models
from kollektiv.models import kollektiv
from studentby.models import studentby

# Create your models here.

class bruker(models.Model):
    brukernavn = models.CharField(max_length=30)
    isManager = models.BooleanField()
    studentby = studentby()
    kollektiv = models.ForeignKey(kollektiv(), on_delete=models.CASCADE)
    def __str__(self):
        return self.brukernavn


