# Realizar un programa que reciba la información de un vehículo :
# -Marca
# -Color
# -Cilindraje
# Imprimir el nombre, valor de cada variable y el tipo de cada variable.
# Author: Jhon Alexis Piracoca Arcos

print("VEHICULOS")
brand = input("Digite la marca del vehiculo:")
color = input("Digite el color del vehiculo:")
cylinder = float(input("Digite el clindraje del vehiculo:"))

print(f"Marca = {brand}, Tipo = {type(brand)}")
print(f"Color = {color}, Tipo = {type(color)}")
print(f"Cilindraje = {cylinder}, Tipo = {type(cylinder)}")