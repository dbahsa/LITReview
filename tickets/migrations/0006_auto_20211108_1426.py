# Generated by Django 3.2.9 on 2021-11-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20211104_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
