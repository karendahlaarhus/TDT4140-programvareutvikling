from django.db import models
from kollektiv.models import kollektiv
from studentby.models import studentby


class bruker(models.Model):
    brukernavn = models.CharField(max_length=30)
    passord = models.CharField(max_length=30, default="passord",null=False)
    isManager = models.BooleanField()
    studentby = studentby()
    kollektiv = models.ForeignKey(kollektiv(), null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.brukernavn


