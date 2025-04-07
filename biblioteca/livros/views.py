from django.shortcuts import render
from .models import Livro

# Create your views here.


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})
