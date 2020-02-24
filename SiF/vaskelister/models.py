# Create your models here.
from django.urls import reverse
from django.db import models


from SiF.studentby.models import studentby
from SiF.kollektiv.models import kollektiv


class TaskList(models.Model):
    name = models.CharField(max_length=30)
    studentby = models.ForeignKey(studentby, on_delete=models.CASCADE)
    kollektiv = models.ForeignKey(kollektiv, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Task Lists"

        # Prevents (at the database level) creation of two lists with the same kollektiv in the same studentby
        unique_together = ("kollektiv", "studentby")


class Task(models.Model):
    title = models.CharField(max_length=140)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)

    note = models.TextField(blank=True, null=True)

    # Has due date for an instance of this object passed?
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo:task_detail", kwargs={"task_id": self.id})

    # Auto-set the Task creation
    def save(self, **kwargs):
        super(Task, self).save()
