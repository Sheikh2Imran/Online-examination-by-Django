from django.db import models
from django.contrib.postgres.indexes import BrinIndex

from questions.models import Question


class ExamManager(models.Manager):
    def get_published_exams(self):
        return self.filter(is_published=True)


class Exam(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    time = models.FloatField(help_text='total time should be in minutes')
    is_published = models.BooleanField(default=False)

    objects = ExamManager()

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "Exam title: {}".format(self.title)


class ExamQuestionManager(models.Manager):
    def get_exam_questions(self, exam_id):
        return self.filter(exam__id=exam_id).order_by('id')


class ExamQuestion(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = ExamQuestionManager()

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "{} || {}".format(self.exam, self.question)


