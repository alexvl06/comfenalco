# Generated by Django 4.0 on 2022-02-24 06:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Products', '0004_remove_client_email_remove_client_firstname_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.user')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]