# Generated by Django 4.0 on 2022-02-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20220221_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]