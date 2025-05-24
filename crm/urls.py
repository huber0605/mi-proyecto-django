from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar-servicio/', views.registrar_servicio, name='registrar_servicio'),
    path('registrar-cita/', views.registrar_cita, name='registrar_cita'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),  # 👈 esta línea es nueva
]

