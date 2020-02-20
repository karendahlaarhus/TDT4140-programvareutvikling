from django.db import models
from studentby.models import studentby



# Create your models here.

class kollektiv(models.Model):
    kollektivNr = models.PositiveIntegerField(null=False)
    studentby = models.ForeignKey(studentby(),on_delete=models.CASCADE)
    def __str__(self):
        return self.studentby.__str__()+" "+str(self.kollektivNr)

