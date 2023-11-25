from django.contrib import admin
from .models import *

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'furniture_model', 'category', 'location',  'published']
    list_filter = ['category', 'location', 'furniture_model', 'published']
    list_editable = ['published']
    search_fields = ['name']


admin.site.register(Size, SizeAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(FurnitureModel)