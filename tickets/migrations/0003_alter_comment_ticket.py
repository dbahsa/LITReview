# Generated by Django 3.2.8 on 2021-10-29 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20211029_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.ticket'),
        ),
    ]
