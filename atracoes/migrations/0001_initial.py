# Generated by Django 2.1.5 on 2019-01-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('horario_func', models.CharField(max_length=20)),
                ('idade_minima', models.IntegerField()),
            ],
        ),
    ]
