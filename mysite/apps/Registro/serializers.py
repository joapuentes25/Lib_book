from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields=['titulo', 'año', 'precio', 'autor', 'descripcion', 'tipo']