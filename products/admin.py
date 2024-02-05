from django.contrib import admin
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'date']
    list_editable = ['price']
    prepopulated_fields = {'slug': ['title']}
    list_filter = ['price']


class ProCatAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']
    list_editable = ['url_title']


class ProColorAdmin(admin.ModelAdmin):
    list_display = ['color', 'url_color']
    list_editable = ['url_color']
    prepopulated_fields = {'url_color': ['color']}


class ProStyleAdmin(admin.ModelAdmin):
    list_display = ['style', 'url_style']
    list_editable = ['url_style']
    prepopulated_fields = {'url_style': ['style']}


class ProTagAdmin(admin.ModelAdmin):
    list_display = ['tag']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProCatAdmin)
admin.site.register(models.ProductTag, ProTagAdmin)
admin.site.register(models.ProductColor, ProColorAdmin)
admin.site.register(models.ProductStyle, ProStyleAdmin)
