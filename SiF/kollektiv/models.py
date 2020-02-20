from django.db import models
from studentby.models import studentby



# Create your models here.

class kollektiv(models.Model):
    kollektivNr = models.IntegerField(null=False)
    studentby = models.ForeignKey(studentby(),on_delete=models.CASCADE)

