from django.contrib import admin

from .models import (
    Product,
    ProductImagen,
    Trademark,
    Category,
    SubCategory,
    TC
)

# Register your models here.

@admin.register(TC)
class TCAdmin(admin.ModelAdmin):
    """
    Gestor de TC
    """
    list_display = [
        'pk',
        'tc',
        'created_at',
        'update_at'
    ]
    list_display_links = [
        'pk',
        'tc',
    ]

@admin.register(Trademark)
class TrademarkAdmin(admin.ModelAdmin):
    """
    Gestor de Trademark
    """
    list_display = [
        'pk',
        'title',
        'is_active',
        'created_at',
        'update_at',
    ]
    list_display_links = [
        'pk',
        'title',
    ]
    list_editable = [
        'is_active',
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Gestor de Category
    """
    list_display = [
        'pk',
        'title',
        'is_active',
        'created_at',
        'update_at',
    ]
    list_display_links = [
        'pk',
        'title',
    ]
    list_editable = [
        'is_active',
    ]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """
    Gestor de SubCategory
    """
    list_display = [
        'pk',
        'title',
        'is_active',
        'category',
        'created_at',
        'update_at'
    ]
    list_display_links = [
        'pk',
        'title'
    ]
    list_filter = [
        'category',
    ]

