from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
def registro_usuarios(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_usuarios(request):

    """
    
    -> Autentica um usuário e retorna tokens JWT se as credenciais forem válidas.
    
    -> Credenciais solicitadas: username e senha.

    -> Se as credenciais forem válidas, retorna os tokens JWT de acesso e refresh.

    -> Se as credenciais forem inválidas, retorna um erro de autenticação. 

    """


    # Os dados estão sendo serializados (transformados em json) para serem enviados na requisição.
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Se o serializer for válido, ele irá pegar os dados do usuário e autenticar.
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    usuario = authenticate(username=username, password=password)
    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            # Se o usuário for encontrado, ele irá gerar os tokens JWT e retornar na resposta.
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    return Response({'Erro': 'Credenciais Inválidas!'}, status=status.HTTP_401_UNAUTHORIZED)
