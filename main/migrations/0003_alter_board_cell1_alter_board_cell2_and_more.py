# Generated by Django 4.0.3 on 2022-03-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_game_player1_alter_game_player2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='cell1',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell2',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell3',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell4',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell5',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell6',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell7',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell8',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='cell9',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
