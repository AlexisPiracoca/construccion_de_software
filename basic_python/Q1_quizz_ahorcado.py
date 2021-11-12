# Con las imagenes que se encuentran en el siguiente archivo realizar el juego del ahorcado
# Author: Jhon Alexis Piracoca Arcos

import random

IMAGENES = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']

# print(IMAGENES[5])

palabras = ["ahorcado", "computador", "inteligencia", "programar", "apagar"]

def seleccionar_palabra(palabras):
    palabra = random.randint(0, len(palabras) -1)
    return palabras[palabra]   

def ahorcado(IMAGENES, letra_incorrecta, letra_correcta, palabra_random):
    print(IMAGENES[len(letra_incorrecta)])
    print("")

    print("Letras incorrectas:", end=" ") 
    for l in letra_incorrecta:
        print(l, end=" ")
    print("")

    espacio_libre = "_" * len(palabra_random)

    for i in range(len(palabra_random)):
        if palabra_random[i] in letra_correcta:
            espacio_libre = espacio_libre[:i] + palabra_random[i] + espacio_libre[i+1:] 
    
    for l in espacio_libre:
        print(l, end=" ")
    print("")    

def inserte_letra(letra):
    while True:
        l = input("Introduce una letra:")
        l = l.lower()
        if len(l) != 1:
            print("Solo se puede una letra a la vez")
        elif l in letra:
            print("Letra ya usada")
        elif l not in 'abcdefghijklmnopqrstuvwxyz':
            print("Introduce otra letra:")
        else:
            return l 

print ('|| Bienvenido al juego del ahorcado ||')
letra_incorrecta = ""
letra_correcta = ""
palabra_random = seleccionar_palabra(palabras)
fin_juego = False

while True:
    ahorcado(IMAGENES, letra_incorrecta, letra_correcta, palabra_random)
    l = inserte_letra(letra_incorrecta + letra_correcta)
    if l in palabra_random:
        letra_correcta = letra_correcta + l
        letras_halladas = True
        for i in range(len(palabra_random)):
            if palabra_random[i] not in letra_correcta:
                letras_halladas = False
                break
        if letras_halladas:
            print("Felicidades la palabra del ahorcado era:", palabra_random )
            print("-- HAS GANADO EL JUEGO --")    
            fin_juego = True 

    else:
        letra_incorrecta = letra_incorrecta + l
        if len(letra_incorrecta) == len(IMAGENES) - 1:
            ahorcado(IMAGENES, letra_correcta, letra_incorrecta, palabra_random)
            print("Se ha quedado sin intentos. La palabra que tenia que adivinar era:", palabra_random)
            fin_juego = True        

    if fin_juego:
        break