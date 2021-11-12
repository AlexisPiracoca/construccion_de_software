# Programa que reciba el valor de tres productos y calcule el iva.
# En la impresión debe aparecer el total de los productos, el valor del iva y el total.
# Author: Jhon Alexis Piracoca Arcos

product1 = int(input("Digite el valor del primer producto:"))
product2 = int(input("Digite el valor del segundo producto:"))
product3 = int(input("Digite el valor del tercer producto:"))

total_products = product1 + product2 + product3
vat = total_products * 0.19
total = total_products + vat

print("Valor de los productos:", total_products)
print("Iva:", vat)
print("Total:", total)