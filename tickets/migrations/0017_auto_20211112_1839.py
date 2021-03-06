# Generated by Django 3.2.9 on 2021-11-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0016_rename_comment_ticketreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketreview',
            name='rating',
            field=models.CharField(choices=[('0', '- 0'), ('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')], max_length=1),
        ),
        migrations.AlterField(
            model_name='ticketreview',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
