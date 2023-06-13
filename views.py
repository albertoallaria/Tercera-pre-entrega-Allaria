from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Validar los datos y crear el usuario
        usuario = User.objects.create_user(username=username, password=password, email=email)
        
        # Realizar otras acciones necesarias
        
        return redirect('inicio')
    
    return render(request, 'registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('portal')
        else:
            # Mostrar mensaje de error
            error_message = "Usuario o contraseña incorrectos."
            return render(request, 'inicio_sesion.html', {'error_message': error_message})
            
    return render(request, 'inicio_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def portal_digital(request):
    # Lógica para cargar los datos del portal digital y enviarlos a la plantilla
    data = {
        'usuario': request.user,
        # Otras variables necesarias para el portal digital
    }
    
    return render(request, 'portal.html', data)
