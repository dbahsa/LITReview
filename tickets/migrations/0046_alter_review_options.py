# Generated by Django 3.2.9 on 2021-11-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0045_auto_20211119_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created'], 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]