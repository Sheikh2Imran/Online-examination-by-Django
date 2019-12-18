from django.contrib import admin

from questions.models import Subject, Question

admin.site.register(Subject)
admin.site.register(Question)
