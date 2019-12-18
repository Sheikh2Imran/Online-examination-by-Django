from django.db import models
from django.contrib.postgres.indexes import BrinIndex

from exam.models import ExamQuestion
from questions.models import Subject


class UserManager(models.Manager):

    def get_or_create_user(self, name, email):
        try:
            obj, created = User.objects.get_or_create(name=name, email=email)
            return obj
        except Exception as e:
            return False


class User(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)

    objects = UserManager()

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "Username: {}".format(self.name)


class UserAnswerManager(models.Manager):

    def store_user_answer(self, session_data, requested_data):
        try:
            user = User.objects.get(id=session_data['user_id'])
            subject = Subject.objects.get(id=session_data['subject_id'])
            return self.create(
                user=user, subject=subject, question=requested_data['question'], answer=requested_data['user_answer'])
        except Exception as e:
            print(e)
            return False


class UserAnswer(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)

    objects = UserAnswerManager()

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "{} || Answer: {}".format(self.user, self.answer)


class UserResult(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    score = models.FloatField()
    time_spent = models.FloatField(help_text='time should be in minutes')

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "{} || score: {} || Time spent: {} || {}".format(self.user, self.score, self.time_spent, self.exam_question)
