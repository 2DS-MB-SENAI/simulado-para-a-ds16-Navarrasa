from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    
    """
    
    -> CustomUser -> classe que herda alguns atributos do modelo AbstractUser
    do Django, como username e password.

    -> O modelo AbstractUser já possui os campos username, password, first_name e last_name.
    
    -> O campo telefone foi adicionado para armazenar o número de telefone do
    usuário. 
    
    -> O campo telefone é opcional e pode ser deixado em branco.
    
    -> O campo telefone é um CharField com tamanho máximo de 15 caracteres.
    
    """
    
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username