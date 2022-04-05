from django.contrib import admin

from .models import Category, City, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'city', 'created', 'updated', 'views']
    prepopulated_fields = {'slug': ['title', 'category']}
    list_filter = ['category']
    search_fields = ['title']
