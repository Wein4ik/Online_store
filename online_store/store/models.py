from django.db import models
#import random
from django.urls import reverse


class Product(models.Model):
    """Товары"""
    # def gen_article(self):
    #     l = self.color[:2].upper()
    #     l += str(random.randint(1000, 9999))
    #     l += self.color[:2].upper()
    #     return l

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.FloatField()
    avail = models.BooleanField(default=True)
    size = models.ForeignKey('Shoe_sizes', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE)
    type = models.ForeignKey('Cat_types', on_delete=models.CASCADE)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    gender = models.ForeignKey('Genders', on_delete=models.CASCADE)
    color = models.ForeignKey('Colors', on_delete=models.CASCADE)
    article = models.CharField(max_length=50, default='1')
    image = models.ImageField(upload_to=f'products/', null=True)
    url = models.SlugField(max_length=160, unique=False)
    count = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Categories(models.Model):
    """Категории"""
    name = models.CharField(max_length=255)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Cat_types(models.Model):
    """Типы категорий"""
    name = models.CharField(max_length=255)
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type", kwargs={"url": self.url})

    class Meta:
        verbose_name = 'Тип категории'
        verbose_name_plural = 'Типы категорий'


# class Clothing_sizes(models.Model):
#     value = models.CharField(max_length=5)

class Shoe_sizes(models.Model):
    """Размеры обуви"""
    value = models.CharField(max_length=5)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Размер обуви'
        verbose_name_plural = 'Размеры обуви'
        ordering = ['value']


class Countries(models.Model):
    """Страны производители"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна производитель'
        verbose_name_plural = 'Страны производители'


class Genders(models.Model):
    """Пол"""
    name = models.CharField(max_length=7)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Colors(models.Model):
    """Цвета"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Brands(models.Model):
    """Бренды"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'