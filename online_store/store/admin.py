from django.contrib import admin
from .models import *


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',
                    'avail', 'size', 'brand', 'type',
                    'gender', 'article', 'count')
    list_filter = ('type', 'size', 'brand', 'gender')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cat_types)
class Cat_typesAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat')


@admin.register(Shoe_sizes)
class Shoe_sizesAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_filter = ('value',)


@admin.register(Countries)
class Countries(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Genders)
class Countries(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Colors)
class Countries(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductsAdmin)
