# Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario 
# ingrese el número 0 (detener las preguntas ante este escenario).
# Author: Jhon Alexis Piracoca Arcos

suma = 0
numero = int(input("Ingrese un número:"))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número:")) 
    if (numero == 0):
        break
print(f"Suma total:",suma)
print("|| Programa finalizado ||")