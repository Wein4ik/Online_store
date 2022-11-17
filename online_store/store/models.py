from django.db import models
import random


class Product(models.Model):

    def gen_article(self):
        l = self.color[:2].upper()
        l += str(random.randint(1000, 9999))
        l += self.color[:2].upper()
        return l

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    avail = models.BooleanField(default=True)
    size = models.IntegerField()
    brand = models.CharField(max_length=255)
    type = models.ForeignKey('Cat_types', on_delete=models.CASCADE)
    country = models.ForeignKey('Countries', on_delete=models.CASCADE)
    gender = models.ForeignKey('Genders', on_delete=models.CASCADE)
    color = models.ForeignKey('Colors', on_delete=models.CASCADE)
    article = models.CharField(max_length=50, default=gen_article())


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cat_types(models.Model):
    name = models.CharField(max_length=255)
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Clothing_sizes(models.Model):
#     value = models.CharField(max_length=5)

class Shoe_sizes(models.Model):
    value = models.CharField(max_length=5)


class Countries(models.Model):
    name = models.CharField(max_length=50)


class Genders(models.Model):
    name = models.CharField(max_length=7)
