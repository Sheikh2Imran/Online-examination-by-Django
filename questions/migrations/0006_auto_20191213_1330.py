# Generated by Django 3.0 on 2019-12-13 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20191213_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='subject_id',
            new_name='subject',
        ),
    ]
