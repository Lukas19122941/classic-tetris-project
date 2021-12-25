# Generated by Django 3.1.3 on 2021-04-17 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0048_auto_20210417_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmatch',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='classic_tetris_project.tournamentplayer'),
        ),
        migrations.AlterField(
            model_name='tournamentmatch',
            name='player1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='classic_tetris_project.tournamentplayer'),
        ),
        migrations.AlterField(
            model_name='tournamentmatch',
            name='player2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='classic_tetris_project.tournamentplayer'),
        ),
        migrations.AlterField(
            model_name='tournamentmatch',
            name='source1_data',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentmatch',
            name='source2_data',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentmatch',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='classic_tetris_project.tournamentplayer'),
        ),
    ]
