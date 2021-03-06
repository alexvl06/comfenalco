# Generated by Django 4.0 on 2022-02-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.PositiveIntegerField()),
                ('img', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=10)),
            ],
        ),
    ]
