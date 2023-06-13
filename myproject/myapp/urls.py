from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('iniciar/', views.iniciar_sesion, name='iniciar_sesion'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta raíz del proyecto
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('iniciar/', views.iniciar_sesion, name='iniciar_sesion'),
]
