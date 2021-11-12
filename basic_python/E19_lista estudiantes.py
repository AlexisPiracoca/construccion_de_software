# Crear una lista con información de estudiantes. Un estudiante cuenta con
# nombres,
# código,
# teléfono.
# Historias de usuario
# 1. Como docente quiero imprimir la información de los estudiantes para conocerlos.
# 2. como docente quiero buscar un estudiante por teléfono para llamarlo
# 3. Como docente quiero buscar un estudiante por nombre para consultar su información
# 4. como docente quiero buscar todas las personas por nombre el resultado deseo imprimirlo en una nueva lista
# 5. como docente quiero eliminar de la lista la información de un estudiante por nombre
# 6. como docente quiero agregar a un nuevo estudiante en la lista para consultar su información mas adelante.
# Author: Jhon Alexis Piracoca Arcos

def ingresarNombre():
    """ Funcion para añadir un nombre """
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre=="":
            print("El nombre no puede estar vacio")
        else:
            return nombre


def ingresarTelefono():
    """ Funcion para añadir una nota """
    while True:
        try:
            telefono = int(input("Ingrese el telefono del estudiante:"))
            return telefono
        except:
            print("El telefono tiene que ser un valor numerico")


def ingresarCodigo():
    """ Funcion para añadir un codigo """
    while True:
        try:
            codigo = int(input("Ingrese el codigo del estudiante:"))
            return codigo
        except:
            print("El codigo tiene que ser un valor numerico")

def mostrarEstudiante():
    nombre = ingresarNombre()
    for el in estudiantes:
        if el[0] == nombre:
            print("El nombre del estudiante es'{}' y el telofono es {}".format(nombre, el[1]))
            return True
    print("No se encuentra el estudiante")
    return False


def mostrarEstudiante_Telefono():
    telefono = ingresarTelefono()
    for el in estudiantes:
        if el[1] == telefono:
            print("El telefono del estudiante es:'{}' y su nombre es:{}".format(telefono, el[0]))
            return True
    print("No se encuentra el telefono")
    return False

def listarEstudiantesNombre():
    estudiantes.sort()
    print("\n".join(i[0]+" - "+str(i[1])+" - "+str(i[2]) for i in estudiantes))

def listarEstudiantesTelefono():
    """ lista los estudiantes ordenados por su telefono descendente """
    estudiantes.sort(key=lambda x: x[1], reverse=True)
    print("\n".join(i[0]+" - "+str(i[1]) for i in estudiantes))

def borrarEstudiante():
    """ Funcion para borrar un estudiante """
    nombre = ingresarNombre()
    indice = buscarEstudiante(nombre)
    if indice==-1:
        print("No se ha encontrado el estudiante '{}'".format(nombre))
        return False
    print("Se ha eliminado el estudiante '{}' con nombre {}".format(nombre, estudiantes[indice][1]))
    del estudiantes[indice]
    return True

def buscarEstudiante(nombre):
    """Funcion que devuelve el indice de un estudiante en la lista
    Devuelve -1 si no ha encontrado el estudiante"""
    for i,e in nombre(estudiantes):
        if e[0]==nombre:
            return i
    return -1

def Menú():
    print("---------------------------------------------------------------")
    print ("Selecciona una opción...")
    print ("\t1 - Listado de los estudiantes ordenados por el nombre")
    print ("\t2 - Buscar estudiante por nombre")
    print ("\t3 - Buscar estudiante por telefono")
    print ("\t4 - Añadir estudiante")
    print ("\t5 - Borrar un estudiante")
    print ("\t6 - Buscar un estudiante por el nombre")
    print ("\n\t0 - Salir")

estudiantes=[]
while True:
    Menú ()
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion=-1
    if opcion == 1:
       listarEstudiantesNombre()
    elif opcion == 2:
        mostrarEstudiante()
    elif opcion == 3:
        mostrarEstudiante_Telefono()
    elif opcion == 4:
        estudiantes.append((ingresarNombre(), ingresarTelefono(),ingresarCodigo()))
    elif opcion == 5:
        borrarEstudiante()
    elif opcion == 6:
        buscarEstudiante()
    elif opcion == 0:    
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")