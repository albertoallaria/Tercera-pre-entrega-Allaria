import json

def registrar_usuario(usuarios):
    nombre = input("Ingrese su Nombre: ")
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su Contraseña: ")
    telefono = input("Ingrese su teléfono: ")
    direccion_facturacion = input("Ingrese su dirección actual: ")
    usuario = {
        "nombre": nombre,
        "email": email,
        "password": password,
        "telefono": telefono,
        "direccion_facturacion": direccion_facturacion
    }
    usuarios.append(usuario)
    print("El usuario ha sido registrado exitosamente")

def iniciar_sesion(usuarios):
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario["email"] == email and usuario["password"] == password:
            print("Inicio de sesión exitoso")
            return
    print("El correo electrónico o la contraseña son incorrectos")

def datos_facturar(direccion_facturacion, telefono):
    direccion_fac = {
        "direccion": direccion_facturacion,
        "telefono": telefono
    }
    return direccion_fac

def cargar_datos(datos):
    direccion_facturacion = input("Ingrese su dirección actual: ")
    telefono = input("Ingrese su teléfono: ")
    datos_fac = datos_facturar(direccion_facturacion, telefono)
    datos.append(datos_fac)
    
def main():
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = []

    while True:
        print("1. Registrar un nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            iniciar_sesion(usuarios)
        elif opcion == "3":
            with open("usuarios.json", "w") as archivo:
                json.dump(usuarios, archivo)
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    main()
