
from django.db import models

class Vaskeliste(models.Model):
    name = models.CharField(max_length=20, default="Ukjent", null=False)
    week = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Vaskelister"
    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    vaskeliste = models.ForeignKey(Vaskeliste(), on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.text


