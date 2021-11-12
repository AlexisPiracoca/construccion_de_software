# Author: Jhon Alexis Piracoca Arcos

lista_temperatura_tunja = [4.5, 21, 7, 15, 10, 5, 22, 19, 4, 3]

def promedio(lista):
    suma = 0
    for valor in lista:
        suma += valor
    promedio = suma/len(lista)
    return promedio

def min_max(lista):
    min = 100
    max = 10
    for valor in lista:
        if valor < min:
            min = valor
        if valor > max:
            max = valor
    return min, max

def mediana(lista):
    lista.sort()
    mediana = 0
    longitud = len(lista)
    mitad = int(longitud/2)
    if longitud == 0:
        mediana = (lista[mitad]+lista[mitad-1])/2
        return mediana
    else:
        return lista[mitad]    

min, max = min_max(lista_temperatura_tunja)
promedio = promedio(lista_temperatura_tunja)
mediana = mediana(lista_temperatura_tunja)

print(f"La temperatura minima es: {min} y la temperatura máxima es: {max}")
print(f"El premdio de la temperatura es: {promedio}")
print(f"La mediana es: {mediana}")