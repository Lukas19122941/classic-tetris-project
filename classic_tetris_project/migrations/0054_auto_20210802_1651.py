# Generated by Django 3.1.3 on 2021-08-02 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0053_auto_20210607_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournamentmatch',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='classic_tetris_project.match'),
        ),
    ]
