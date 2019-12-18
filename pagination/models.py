from django.db import models

from questions.models import Question


class PaginationManager(models.Manager):
    def create_pagination(self, session_data):
        total_obj = Question.objects.filter(subject_id=session_data['subject_id']).count()
        return self.create(user_id=session_data['user_id'], total_obj=total_obj, subject_id=session_data['subject_id'])

    def update_pagination(self, session_data):
        pagination_data = self.get(user_id=session_data['user_id'], subject_id=session_data['subject_id'])
        start = pagination_data.start + 1
        end = pagination_data.end + 1
        updated_data = self.filter(user_id=session_data['user_id'], subject_id=session_data['subject_id']).update(
            start=start, end=end)
        if updated_data:
            return self.get(user_id=session_data['user_id'], subject_id=session_data['subject_id'])


class Pagination(models.Model):
    user_id = models.IntegerField()
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=1)
    total_obj = models.IntegerField()
    subject_id = models.IntegerField(null=True)

    objects = PaginationManager()