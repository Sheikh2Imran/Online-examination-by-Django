from django.db import models
from django.contrib.postgres.indexes import BrinIndex


class Subject(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    subject_name = models.CharField(max_length=50, null=False, blank=False)

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

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "Subject: {} | Question: {}".format(self.subject, self.question)


class Answer(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "{} | Answer: {}".format(self.question, self.answer)


class Option(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=100, default="")
    option2 = models.CharField(max_length=100, default="")
    option3 = models.CharField(max_length=100, default="")
    option4 = models.CharField(max_length=100, default="")

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "{} | Options: {} | {} | {} | {}".format(
            self.question, self.option1, self.option2, self.option3, self.option4)