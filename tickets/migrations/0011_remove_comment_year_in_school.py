# Generated by Django 3.2.9 on 2021-11-08 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_comment_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='year_in_school',
        ),
    ]