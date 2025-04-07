from django.urls import path
from .views import registro_usuarios, login_usuarios

urlpatterns = [
    path('registro/', registro_usuarios, name='registro'),
    path('login/', login_usuarios, name='login'),
]
