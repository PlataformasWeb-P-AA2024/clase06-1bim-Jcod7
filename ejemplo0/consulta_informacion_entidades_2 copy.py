"""
    Consulta de información en las entidades en la base de datos
"""

from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute



# hace consultas a la base de datos
cadena_consulta_sql = "SELECT * from Autor"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
#Estamos inerando en informacion para mostrar el nombre y la edad 
for d in informacion:
    print("El nombre es: %s y la edad es %d"(d[0],d[3]))
#   print("%s - %s - %s - %d" % (d[0], d[1], d[2], d[3]))
#print(informacion)

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
