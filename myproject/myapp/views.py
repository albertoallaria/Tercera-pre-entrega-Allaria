from django.shortcuts import render, redirect
from .models import Usuario

def usuarios(request):
    # Aquí va la lógica para manejar la solicitud de la ruta /usuarios/
    # Puedes agregar el código necesario para mostrar o procesar los datos de los usuarios.
    # Por ejemplo:
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def registrar_usuario(request):
    if request.method == 'POST':
        # Código para registrar un nuevo usuario
        return redirect('inicio')
    return render(request, 'registrar_usuario.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        # Código para iniciar sesión
        return redirect('inicio')
    return render(request, 'iniciar_sesion.html')

def index(request):
    return render(request, 'index.html')
