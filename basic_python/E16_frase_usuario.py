# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
# indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
# Author: Jhon Alexis Piracoca Arcos

frase = input("Digite su frase: ")
letra = input("Digite la letra para buscar su posición:")
i = 0
while i!= len(frase):
    if letra != frase[i]:
        print("No se encontró en la posición", i)
        i += 1
        continue
    print("Se encontró en la posición", i)
    break