# Author: Jhon Alexis Piracoca Arcos

def suma(a,b):
    return a+b

print(suma(2,2))

def acceso(año_nacimiento):
    edad = 2021-año_nacimiento
    if edad >=18:
        print("Bienvenido al establecimiento")
    else:
        print("No se le permite el acceso")

acceso(2002)


    