# Generated by Django 5.0.3 on 2024-04-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=300, upload_to='', verbose_name='Изображение товара'),
        ),
    ]