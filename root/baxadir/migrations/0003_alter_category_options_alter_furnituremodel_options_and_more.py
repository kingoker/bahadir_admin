# Generated by Django 4.2.7 on 2023-11-20 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baxadir', '0002_remove_category_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='furnituremodel',
            options={'verbose_name': 'Модель товара', 'verbose_name_plural': 'Модели товаров'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'РАЗМЕР', 'verbose_name_plural': 'РАЗМЕРЫ'},
        ),
        migrations.AddField(
            model_name='size',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='furnituremodel',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='furniture_images/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='furnituremodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='furnituremodel',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='location',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='size',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baxadir.category', verbose_name='Категория товара'),
        ),
        migrations.AlterField(
            model_name='size',
            name='furniture_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baxadir.furnituremodel', verbose_name='Модель товара'),
        ),
        migrations.AlterField(
            model_name='size',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baxadir.location', verbose_name='Помещение'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='size',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='size',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
