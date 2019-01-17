# Generated by Django 2.1.5 on 2019-01-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('linha1', models.CharField(max_length=150)),
                ('linha2', models.CharField(blank=True, max_length=150, null=True)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=100)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
