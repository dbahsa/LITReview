# Generated by Django 3.2.9 on 2021-11-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0020_rename_rating_ticketreview_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketreview',
            name='rate',
            field=models.CharField(choices=[('0', '- 0'), ('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')], max_length=1),
        ),
    ]