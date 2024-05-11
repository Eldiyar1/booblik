from django.contrib import admin
from .models import Menu, Product


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = [
        ('Русский перевод', {
            'fields': ['name']
        }),
        ('Кыргызский перевод', {
            'fields': ['name_ky']
        }),
        ('Английский перевод', {
            'fields': ['name_en']
        }),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'price', 'unit', 'menu')
    search_fields = ('title', 'description')
    list_filter = ('menu',)
    fieldsets = [
        ('Русский перевод', {
            'fields': ['title', 'description', 'image', 'price', 'menu']
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'description_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en']
        })
    ]
