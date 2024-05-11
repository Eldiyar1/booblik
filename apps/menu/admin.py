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
    list_display = (
        'title', 'price', 'promotional_price', 'get_current_price', 'promotion_start_date', 'promotion_end_date',
        'recommended', 'liters', 'menu')
    search_fields = ('title', 'description')
    list_filter = ('recommended', 'menu')

    def get_current_price(self, obj):
        return obj.current_price

    get_current_price.short_description = 'Текущая цена'

    fieldsets = [
        ('Основные данные', {
            'fields': ['title', 'description', 'image', 'price', 'promotional_price', 'promotion_start_date',
                       'promotion_end_date', 'recommended', 'liters', 'menu']
        }),
        ('Кыргызский перевод', {
            'fields': ['title_ky', 'description_ky']
        }),
        ('Английский перевод', {
            'fields': ['title_en', 'description_en']
        }),
    ]

    readonly_fields = ['get_current_price']
