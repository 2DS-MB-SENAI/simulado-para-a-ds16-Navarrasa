from django.shortcuts import render
from .models import Livro
from rest_framework.decorators import api_view
from .serializers import LivroSerializer
# from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#  TASK 1 - renderizando template HTML
"""
Cria um objeto livro que pega todos os livros do banco de dados
e renderiza o template livros.html com a lista de livros.
O template livros.html deve estar na pasta templates do app livros.
"""
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros},status=status.HTTP_200_OK)


"""
Criando e listando Livros a partir de uma API REST
1. Criando um livro
2. Listando livros
3. Retornando códigos HTTP de acordo com a operação
--------------------------------------------------------------------------
1.1 Criando um objeto "livros" que pega todos os livros do banco de dados
2.1 Criando um serializer para o modelo Livro
3.1 Criando uma view para listar os livros
4.1 Criando uma view para criar um livro
"""

# TASK 2 - GET & POST
@api_view(['GET', 'POST'])
def listar_livros_api(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class LivroListCreateAPIView(ListCreateAPIView):
#     queryset = Livro.objects.all()
#     serializer_class = LivroSerializer