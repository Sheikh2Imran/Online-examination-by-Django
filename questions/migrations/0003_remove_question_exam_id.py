# Generated by Django 3.0 on 2019-12-13 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20191213_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='exam_id',
        ),
    ]
