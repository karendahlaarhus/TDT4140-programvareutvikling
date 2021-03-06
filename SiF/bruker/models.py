from django.db import models
from kollektiv.models import kollektiv


class bruker(models.Model):
    brukernavn = models.CharField(max_length=30, unique=True)
    passord = models.CharField(max_length=30, default="passord",null=False)
    isManager = models.BooleanField()
    kollektiv = models.ForeignKey(kollektiv(), null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.brukernavn
    class Meta:
        verbose_name_plural = "Brukere"



