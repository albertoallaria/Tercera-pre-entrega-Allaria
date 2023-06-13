from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registro'),
    path('inicio/', views.iniciar_sesion, name='inicio'),
    path('cerrar/', views.cerrar_sesion, name='cerrar'),
    path('portal/', views.portal_digital, name='portal'),
]
