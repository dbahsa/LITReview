# Generated by Django 3.2.9 on 2021-11-16 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0036_alter_userfollows_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='comment',
        ),
    ]