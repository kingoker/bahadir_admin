from django.db import models


# Помещение
class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return self.name


# Категория
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


# Модель
class FurnitureModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='furniture_images/', default='default_image.jpg', verbose_name='Фотография')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Модель товара'
        verbose_name_plural = 'Модели товаров'

    def __str__(self):
        return self.name


# Размер
class Size(models.Model):
    name = models.CharField(max_length=255, verbose_name='Размер')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    cost = models.IntegerField(default=0, verbose_name='Цена')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Помещение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    furniture_model = models.ForeignKey(FurnitureModel, on_delete=models.CASCADE, verbose_name='Модель товара')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'ТОВАР'
        verbose_name_plural = 'ТОВАРЫ'

    def __str__(self):
        return self.name

