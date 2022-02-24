# Generated by Django 4.0 on 2022-02-24 07:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Products', '0005_rename_products_product_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(default='silueta.png', upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
        migrations.CreateModel(
            name='Solicitude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('quantity', models.PositiveBigIntegerField(verbose_name='Cantidad')),
                ('pendiente', models.BooleanField(verbose_name='En proceso')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='Products.product', verbose_name='Producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='auth.user', verbose_name='Usuario')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
