# Generated by Django 3.2.9 on 2021-11-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0054_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
