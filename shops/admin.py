from django.contrib import admin

from .models import Shop, Street, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('name', 'city')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city')
