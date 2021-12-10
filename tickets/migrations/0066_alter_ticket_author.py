# Generated by Django 3.2.9 on 2021-12-03 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('tickets', '0065_alter_ticket_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]