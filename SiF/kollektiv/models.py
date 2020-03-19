from django.db import models
from studentby.models import studentby


class kollektiv(models.Model):
    kollektivNr = models.PositiveIntegerField(null=False)
    studentby = models.ForeignKey(studentby(),on_delete=models.CASCADE)

    def __str__(self):
        return self.studentby.__str__()+" nr "+str(self.kollektivNr)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['kollektivNr','studentby'], name='unique_kollektiv'),
        ]
        verbose_name_plural = "Kollektiv"




