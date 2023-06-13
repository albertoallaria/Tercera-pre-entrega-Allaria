from django.shortcuts import render, redirect
from .models import Usuario

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        password = request.POST['password']
        telefono = request.POST['telefono']
        direccion_facturacion = request.POST['direccion_facturacion']
        usuario = Usuario(nombre=nombre, email=email, password=password, telefono=telefono, direccion_facturacion=direccion_facturacion)
        usuario.save()
        return redirect('inicio')
    return render(request, 'registrar_usuario.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            usuario = Usuario.objects.get(email=email, password=password)
            return redirect('inicio')
        except Usuario.DoesNotExist:
            mensaje = 'El correo electrónico o la contraseña son incorrectos'
            return render(request, 'iniciar_sesion.html', {'mensaje': mensaje})
    return render(request, 'iniciar_sesion.html')


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

