# Generated by Django 2.1.5 on 2019-01-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('pontos_turisticos', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ManyToManyField(to='endereco.Endereco'),
        ),
    ]
