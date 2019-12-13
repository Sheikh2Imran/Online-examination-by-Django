# Generated by Django 3.0 on 2019-12-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20191213_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
