# Generated by Django 3.2.9 on 2021-11-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_remove_comment_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auteur',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentaire',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='note',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='titre',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.CharField(blank=True, max_length=8192),
        ),
        migrations.AddField(
            model_name='comment',
            name='headline',
            field=models.CharField(blank=True, default=None, max_length=128),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('0', '- 0'), ('1', '- 1'), ('2', '- 2'), ('3', '- 3'), ('4', '- 4'), ('5', '- 5')], help_text='Veuillez dérouler le menu ci-dessus pour ajouter votre note', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]