# Author: Jhon Alexis Piracoca Arcos

lista = []
lista = ["Jhon Alexis", 22, 2.5, True]

print(lista)

#operaciones
lista.append("Pedro")
print(lista)

lista.insert(1, "Camilo")
print(lista)

lista.remove("Camilo")
print(lista)

print(lista.pop(2))
print(lista)

print(lista.reverse())
print(lista)

for item in lista:
    print(item)