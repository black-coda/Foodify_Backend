from django.contrib import admin
from main.models import *


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    prepopulated_fields = {
        'slug': ('category_name',)
    }
    ordering = ('-category_name',)
    search_fields = ('category_name',)


admin.site.register(CafetriaType)
admin.site.register(FoodItem)

