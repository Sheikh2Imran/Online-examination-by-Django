from django.db import models
from django.contrib.postgres.indexes import BrinIndex

from questions.models import Question


class Exam(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    time = models.FloatField(help_text='total time should be in minutes')

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "Exam title: {}".format(self.title)


class ExamQuestion(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "{} || {}".format(self.exam, self.question)


