# Author: Jhon Alexis Piracoca Arcos

meses = {
    1:'Enero',
    2:'Febrero',
    3:'Marzo',
    4:'Abril'
}

def get_mes(x):
    mes = meses.get(x)
    if mes == None:
        return "no existe el mes "
    return mes

print(get_mes(4));