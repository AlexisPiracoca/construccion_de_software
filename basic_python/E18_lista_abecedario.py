# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
# que ocupen posiciones múltiplos de 3 y 5, y muestre por pantalla la lista resultante.
# Author: Jhon Alexis Piracoca Arcos

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'ñ', 'o','p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(abecedario), 0, -1):
    if x % 3 & 5 == 0:
        abecedario.pop(x-1)
print(abecedario)