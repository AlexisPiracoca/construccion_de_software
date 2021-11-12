import psycopg2  

class data_base:
    def __init__(self):
        self.connection = psycopg2.connect(
            host = 'localhost',
            database = 'bd_superheroes',
            user = 'postgres',
            password = 'Contrato455' 
        )
        self.cursor = self.connection.cursor()
        print('conexion exitosa')

    def consultas(self):
        sql = "select id, name, año_de_nacimiento from characters where año_de_nacimiento between '2010' and '2020'" 
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            return lista
        except Exception as e:
            raise 

bd = data_base()
lista = bd.consultas()
for personaje in lista:
    print(personaje)   