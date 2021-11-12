from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

lista = [
    {  "id": 1,
        "nombre": "Spider-Man",
        "descripcion":"Emerging from a universe in need of a new Spider-Man, a Brooklyn teen named Miles Morales rose to the challenge. Reluctant at first, he quickly earned the mantle of a Super Hero.",
        "poderes":  "Fuerza, Agilidad",
        "ruta_imagen": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/037smm_com_crd_01.jpg"
    },
    {"id": 2,
     "nombre": "Red Guardian",
     "descripcion": "Alexei is known most famously as Red Room’s answer to Captain America. He’s a Super-Soldier spy who has lived a lifetime of triumph during the Cold War.",
     "poderes": "Fuerza, Agilidad",
     "ruta_imagen": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/435rgd_com_crd_01.jpg"
     },

    {"id": 3,
     "nombre": "Yelena",
     "descripcion": "A product of the Red Room’s ruthless training programs, this fiery assassin has a secret history with the Black Widow that she is determined to address.",
     "poderes": "Fuerza, Agilidad",
     "ruta_imagen": "https://terrigen-cdn-dev.marvel.com/content/prod/1x/433ybv_com_crd_01.jpg"
     },
]

def get_all_personajes(request):
    diccionario = {'titulo': 'Personajes Del Universo Marvel','personajes': lista}   
    return render(request, 'index.html', diccionario)

def buscar_personaje(id):
    for personaje in lista:
        if personaje["id"] == id:
            return personaje   

def get_personaje(request, id):
    html = ''
    personaje = buscar_personaje(id)
    if personaje == None:
        return HttpResponse(f"el personaje con id {id} no existe")
    html +=  f' <h1>  {personaje.get("nombre")}</h1>' \
                 f' <img  alt="{personaje.get("nombre")}" src="{personaje.get("ruta_imagen")}"/>'\
                 f' <p> {personaje.get("descripcion")}</p>'   
    return HttpResponse(html)

def borrar_personaje(request, id):
    personaje = buscar_personaje(id)
    if personaje == None:
        return HttpResponse(f"el personaje con id {id} no existe")   
    lista.remove(personaje)    
    return redirect("/personajes")

def add_personaje(request, id, nombre, ruta_imagen):
    return redirect("/personajes")

def sumar(request, valor1, valor2):
    return HttpResponse(f"<h1> {valor1+valor2} </h1>")

