# Proyecto Web Django

Este es un proyecto web desarrollado con Django, que sigue el patrón MVT (Modelo-Vista-Plantilla).

## Funcionalidades

El proyecto incluye las siguientes funcionalidades:

1. Herencia de HTML: Utiliza una plantilla base `base.html` para compartir elementos comunes en todas las páginas.
2. Modelos: Se han definido 3 clases de modelo en el archivo `models.py`.
3. Formularios de inserción: Se ha creado un formulario para insertar datos en todas las clases de modelo. Puedes acceder a él en la ruta `/insertar/`.
4. Formulario de búsqueda: Se ha creado un formulario para buscar datos en la base de datos. Puedes acceder a él en la ruta `/buscar/`.

## Orden de prueba

Sigue el siguiente orden para probar las funcionalidades:

1. Ejecuta el servidor de desarrollo de Django con el comando `python manage.py runserver`.
2. Abre tu navegador web y accede a `http://localhost:8000/insertar/` para insertar datos en las clases de modelo.
3. Navega a `http://localhost:8000/buscar/` para realizar búsquedas en la base de datos.

## Estructura del proyecto

- `myproject/`: Carpeta principal del proyecto Django.
  - `myapp/`: Carpeta de la aplicación Django.
    - `templates/`: Carpeta que contiene las plantillas HTML.
      - `base.html`: Plantilla base que se hereda en todas las páginas.
      - `insertar.html`: Plantilla del formulario de inserción.
      - `buscar.html`: Plantilla del formulario de búsqueda.
    - `models.py`: Archivo que define los modelos de la base de datos.
    - `views.py`: Archivo que contiene las vistas y la lógica del proyecto.
    - `urls.py`: Archivo de configuración de las URLs de la aplicación.

