from django.urls import path, include
from . import views
#-------------------------API------------------------
from .views import LibroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('libros', LibroViewSet)

urlpatterns = [   
    path('', views.index, name="index"),
    path('listado-libros/', views.listado_libros, name="listado-libros"),
    path('agregar-libro/', views.agregar_libro, name="agregar-libro"),
    path('modificar-libro/<id>/', views.modificar_libro, name="modificar-libro"),
    path('eliminar-libro/<id>/', views.eliminar_libro, name="eliminar-libro"),
    path('eliminar-libro-busqueda/<id>/', views.eliminar_libro_busqueda, name="eliminar-libro-busqueda"),
    path('busqueda/', views.visualizar_busqueda, name="busqueda"),
    path('registro-usuario/', views.registrar_usuario, name="registro-usuario"),
    path('perfil/', views.perfil, name="perfil"),
    path('api/', include(router.urls)), 
]