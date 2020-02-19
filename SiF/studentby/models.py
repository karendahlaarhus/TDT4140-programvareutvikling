from django.db import models

# Create your models here.

class studentby(models.Model):
    #manager =
    # kollektiv = liste med kollektiv
    navn = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
