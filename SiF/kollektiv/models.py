from django.db import models
from studentby.models import studentby
from vaskelister.models import Vaskeliste


class kollektiv(models.Model):
    kollektivNr = models.PositiveIntegerField(null=False)
    studentby = models.ForeignKey(studentby(),on_delete=models.CASCADE)
    vaskeliste = models.OneToOneField(Vaskeliste(), on_delete=models.CASCADE, null=True, blank=True) #kun et kollektiv til en vaskeliste
    def __str__(self):
        return self.studentby.__str__()+" nr "+str(self.kollektivNr)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['kollektivNr','studentby'], name='unique_kollektiv'), #et kollektivNr i en bestemt studentby er unikt
        ]
        verbose_name_plural = "Kollektiv"




