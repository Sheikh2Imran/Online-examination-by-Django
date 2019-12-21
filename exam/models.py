from django.db import models
from django.contrib.postgres.indexes import BrinIndex

from questions.models import Question


class ExamManager(models.Manager):
    def get_all_published_exams(self):
        return self.filter(is_published=True)

    def get_only_allowed_exams(self, exam_ids):
        return self.exclude(is_published=True, id__in=exam_ids)


class Exam(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    total_time = models.FloatField(help_text='total time should be in minutes')
    is_published = models.BooleanField(default=False)

    objects = ExamManager()

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "Exam title: {}".format(self.title)


class ExamQuestionManager(models.Manager):
    def get_exam_question(self, exam_id):
        return self.filter(exam=exam_id)

    def get_first_question(self, exam_id):
        self.set_question_time(exam_id)
        return self.filter(exam__id=exam_id)

    def set_question_time(self, exam_id):
        total_question = self.filter(exam=exam_id).count()
        exam_obj = Exam.objects.get(id=exam_id)
        time_per_question = (exam_obj.total_time/total_question)*60
        self.filter(exam=exam_id).update(time_per_question=time_per_question)


class ExamQuestion(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time_per_question = models.IntegerField(default=0, editable=False)

    objects = ExamQuestionManager()

    class Meta:
        indexes = [
            BrinIndex(fields=['id'])
        ]

    def __str__(self):
        return "{} || {}".format(self.exam, self.question)


