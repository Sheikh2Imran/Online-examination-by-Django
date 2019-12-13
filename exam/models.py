from django.db import models


class Exam(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    time = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "Exam title: {} | time for this exam: {}".format(self.title, self.time)


