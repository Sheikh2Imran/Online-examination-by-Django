from django.contrib import admin

from questions.models import Subject, Question, Answer, Option

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Option)
