from django.contrib import admin
from django.urls import path
from characters.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personajes/', get_all_personajes),
    path('personajes/<int:id>/', get_personaje),
    path('personajes/borrar/<int:id>/', borrar_personaje),
    path('personajes/<int:id>/<str:nombre>/<str:ruta_imagen>/', add_personaje),
    path('sumar/<int:valor1>/<int:valor2>/', sumar)
]