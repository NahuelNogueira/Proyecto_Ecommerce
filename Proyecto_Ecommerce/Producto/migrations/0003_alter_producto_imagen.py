# Generated by Django 4.1.3 on 2022-11-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
