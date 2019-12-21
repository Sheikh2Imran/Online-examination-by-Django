from django.db import models
from django.contrib.postgres.indexes import BrinIndex


class SubjectManager(models.Manager):
    def get_subject(self, subject_name):
        try:
            return self.get(subject_name=subject_name)
        except Exception as e:
            return False


class Subject(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    subject_name = models.CharField(max_length=100, null=False, blank=False)

    objects = SubjectManager()

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "{}".format(self.subject_name)


class Question(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=False, blank=False)
    answer = models.CharField(max_length=200, null=False, blank=False)
    option1 = models.CharField(max_length=200, null=False, blank=False)
    option2 = models.CharField(max_length=200, null=False, blank=False)
    option3 = models.CharField(max_length=200, null=False, blank=False)
    option4 = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "Subject: {} | Question: {}".format(self.subject, self.question)
