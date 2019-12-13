from django.db import models


class Subject(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    subject_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return "Subject ID: {} and subject title: {}".format(self.id, self.subject_name)
