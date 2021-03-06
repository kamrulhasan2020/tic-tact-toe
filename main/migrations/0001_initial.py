# Generated by Django 4.0.3 on 2022-03-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell1', models.CharField(default='empty', max_length=10)),
                ('cell2', models.CharField(default='empty', max_length=10)),
                ('cell3', models.CharField(default='empty', max_length=10)),
                ('cell4', models.CharField(default='empty', max_length=10)),
                ('cell5', models.CharField(default='empty', max_length=10)),
                ('cell6', models.CharField(default='empty', max_length=10)),
                ('cell7', models.CharField(default='empty', max_length=10)),
                ('cell8', models.CharField(default='empty', max_length=10)),
                ('cell9', models.CharField(default='empty', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('player1', models.CharField(default='p1', max_length=100)),
                ('player2', models.CharField(default='p2', max_length=100)),
            ],
        ),
    ]
