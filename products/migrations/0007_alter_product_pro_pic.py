# Generated by Django 5.0.1 on 2024-01-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_pro_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='تصویر محصول'),
        ),
    ]
