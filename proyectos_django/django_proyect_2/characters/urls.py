from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "characters"

urlpatterns = [
     path('',   views.list,   name="list_characters"),
     path('save', views.save, name="save_characters"),
     path('edit/<int:id>', views.edit, name='edit'),
     path('detail/<int:id>', views.detail, name="detail"),
     path('punto_uno', views.puntoUno),
     path('punto_dos',views.puntoDos),
     path('punto_tres',views.puntoTres),
     path('punto_cuatro',views.puntoCuatro),
     path('punto_cinco', views.puntoCinco),
     path('punto_seis', views.puntoSeis),
     path('punto_siete', views.puntoSiete),
     path('punto_ocho', views.puntoOcho),
     path('punto_nueve', views.puntoNueve),
     path('punto_diez', views.puntoDiez),
]
