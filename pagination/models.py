from django.db import models

from exam.models import ExamQuestion


class PaginationManager(models.Manager):
    def create_pagination(self, session_data):
        total_obj = ExamQuestion.objects.filter(exam__id=session_data['exam_id']).count()
        return self.get_or_create(user_id=session_data['user_id'], total_obj=total_obj, exam_id=session_data['exam_id'])

    def update_pagination(self, session_data):
        try:
            pagination_data = self.get(user_id=session_data['user_id'], exam_id=session_data['exam_id'])
            pagination_data.start += 1
            pagination_data.end += 1
            pagination_data.save()
            return self.get(user_id=session_data['user_id'], exam_id=session_data['exam_id'])
        except Exception as e:
            return False


class Pagination(models.Model):
    user_id = models.IntegerField()
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=1)
    total_obj = models.IntegerField()
    exam_id = models.IntegerField()

    objects = PaginationManager()