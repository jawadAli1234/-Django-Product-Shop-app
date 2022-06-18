from django.contrib import admin
from .models import Product, Offers


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offers, OfferAdmin)
admin.site.register(Product, ProductAdmin)
