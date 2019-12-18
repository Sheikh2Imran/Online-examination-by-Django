from django import forms
from django.db import models


class UserForm(forms.Form):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)


class SubjectForm(forms.Form):
    id = models.IntegerField()