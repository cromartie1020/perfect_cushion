from django.contrib import admin

from .models import   Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'image')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'available', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)  
