# En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 1000 Dolares. 
# Realizar un programa que informe de cuantos empleados cobran menos de 500 y
# cuantos más de 500. Informar también del total que gasta la empresa en pagar a sus empleados.
# Author: Jhon Alexis Piracoca Arcos

import random

trabajadores = []

for x in range(100):
    sueldo = random.randrange(100,1000)
    trabajadores.append(sueldo)

contMayor = 0
contMenor = 0
totalNomina = 0
for sueldo in range(len(trabajadores)):
    totalNomina += sueldo
    if sueldo >= 500:
        contMayor+=1
    else:
        contMenor+=1

print(f"Trabajadores con sueldo mayor a 500: {contMayor}")
print(f"Trabajadores con sueldo menor a 500: {contMenor}")
print(f"Total nomina : {totalNomina}")
print("|| Programa finalizado ||")
