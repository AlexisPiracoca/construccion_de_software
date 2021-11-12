# Un video juego cuenta con la información de sus personajes en un archivo de texto.
# Un jugador tiene la posibilidad de seleccionar alguno de los personajes para combatir con las fuerzas del mal.
# Con cada partida el personaje gana un punto en cada una de sus características.
# Al finalizar el juego se debe almacenar la información de los personajes
# Author: Jhon Alexis Piracoca Arcos

import random
import time

with open("personajes.txt", mode="r", encoding="utf-8") as archivo:
    print(next(archivo))

def get_encabezado(ruta_archivo):
    with open("personajes.txt", mode="r", encoding="utf-8") as arhivo:
        encabezado = next(arhivo)
    array_encabezado = encabezado.split(",")
    for index in range(len(array_encabezado)):
        array_encabezado[index] = array_encabezado[index].strip()
    return array_encabezado   

def get_personajes(ruta_archivo):
    archivo = open(ruta_archivo, mode="r")
    lineas = archivo.readlines()
    archivo.close()
    lista_personajes = []
    for index, linea in enumerate(lineas):
        fila = linea.split(",")
        personaje = {"Tipo": fila[0].strip(), "Vida": fila[1].strip(), "Ataque": fila[2].strip(), "Defensa": fila[3].strip(), "Alcance": fila[4].strip()}
        lista_personajes.append(personaje)
    del lista_personajes[0]
    return lista_personajes

def imprimir_personajes(lista):
    for index, personaje in enumerate(lista):
        print(index, "-", personaje["Tipo"])

def combatir(personaje):
    puntaje = random.choice([1, -1])
    caracteristica = random.choice(["Vida", "Ataque", "Defensa", "Alcance"])
    print("Se esta combatiendo")
    time.sleep(3)
    valor = int(personaje.get(caracteristica)) + puntaje
    personaje.update({caracteristica: str(valor)})
    print(valor)
    return personaje

def update(ruta_archivo):
    with open("personajes.txt", mode="r", encoding="utf-8") as archivo:
        archivo.write(f" {encabezado[0]}, {encabezado[1]}, {encabezado[2]}, {encabezado[3]}, {encabezado[4]}\n")
        for personaje in lista:
            archivo.write(f" {personaje['Tipo']}, {personaje['Vida']}, {personaje['Ataque']}, {personaje['Defensa']}, {personaje['Alcance']}\n")
        archivo.close()

lista = get_personajes("personajes.txt")
print("Selecciona uno de los siguientes personajes")
imprimir_personajes(lista)

encabezado = get_encabezado("personajes.txt")
seleccion = int(input("Personaje: "))
print(lista[seleccion])
personaje = lista[seleccion]
combatir(personaje)
print(lista[seleccion])
update()