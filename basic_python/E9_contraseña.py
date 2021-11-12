# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
# introducida por el usuario coincide con la guardada en la variable sin tener en 
# cuenta mayúsculas y minúsculas.
# Author: Jhon Alexis Piracoca Arcos

claveBD = "123456"
print("Login")
nombre = input("Nombre:")
clave = input("Clave:")

if clave == claveBD:
    print("Bienvenido a la plataforma")
else:
    print("Usuario o contraseña incorrectos")    