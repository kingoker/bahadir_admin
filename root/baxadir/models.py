from django.db import models


# Помещение
class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    Category = models.ManyToManyField('Category')

    class Meta:
        verbose_name = '---- Помещение'
        verbose_name_plural = '---- Помещения'

    def __str__(self):
        return self.name


# Категория
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.ManyToManyField('Model')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = '--- Категория товара'
        verbose_name_plural = '--- Категории товаров'

    def __str__(self):
        return self.name


# Модель
class Model(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='furniture_images/', default='default_image.jpg', verbose_name='Фотография')
    size = models.ManyToManyField('Size')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = '-- Модель товара'
        verbose_name_plural = '-- Модели товаров'

    def __str__(self):
        return self.name


# Размер
class Size(models.Model):
    name = models.CharField(max_length=255, verbose_name='Размер')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = '- Размер'
        verbose_name_plural = '- Размеры'

    def __str__(self):
        return self.name


# Цена
class Price(models.Model):
    name = models.IntegerField(default=0, verbose_name='Сумма')
    model = models.ManyToManyField(Model, verbose_name='Модели')
    size = models.ManyToManyField(Size, verbose_name='Модели')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return str(self.name)
    


# Количество
class Count(models.Model):
    name = models.IntegerField(default=0, verbose_name='Кол-во')
    location = models.ForeignKey(Location, verbose_name='Помещение', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name='Размер', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'

    def __str__(self):
        return str(self.name)