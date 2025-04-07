from rest_framework import serializers
from .models import Livro

"""
Serializadores:

Transformam os dados de entrada e saída para o formato JSON.

"""

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        # fields = ['id', 'titulo', 'autor', 'paginas']