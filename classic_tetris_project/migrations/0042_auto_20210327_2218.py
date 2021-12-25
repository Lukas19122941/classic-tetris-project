# Generated by Django 3.1.3 on 2021-03-27 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0041_auto_20210327_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='short_name',
            field=models.CharField(default='', help_text='Used in the context of an event, e.g. "Challenger\'s Circuit"', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(db_index=False, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='event',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='classic_tetris_project.event'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(help_text='Full name of the tournament', max_length=64),
        ),
        migrations.AddConstraint(
            model_name='tournament',
            constraint=models.UniqueConstraint(fields=('event_id', 'slug'), name='unique_event_slug'),
        ),
    ]
