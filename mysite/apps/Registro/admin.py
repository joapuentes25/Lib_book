from django.contrib import admin
from .models import Libro, Profile
# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display=['titulo', 'año', 'precio', 'autor', 'descripcion','tipo']
    search_fields=['titulo', 'año', 'autor']
    list_filter=['año']
    list_per_page=10

admin.site.register(Libro)
admin.site.register(Profile)