# pequena url para listar os livros
from django.urls import path
from .views import listar_livros_api, listar_livros

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('livros/', listar_livros_api, name='listar_livros_api'),
    ]