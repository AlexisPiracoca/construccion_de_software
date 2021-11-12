# Author: Jhon Alexis Piracoca Arcos

persona = {
    "Nombres":"Alexis",
    "Apellidos":"Piracoca",
    "Telefono":"3142258974",
}

#operaciones

print(persona["Nombres"])
print(persona["Apellidos"])

for llave in persona:
    print(f"{llave}:{persona[llave]}")

print(persona.keys())
print(persona.values())

persona.update({"Nombres":"Alexis",})
print(persona)