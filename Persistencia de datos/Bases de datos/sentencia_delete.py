import sqlite3
from sqlite3 import Error

try:
    conexion = sqlite3.connect('db\my_database_0.db')
    print('Conectado exitosamente')
except Error:
    print(Error)

cursor = conexion.cursor()

cursor.execute('DELETE from empleados_empresa where identificacion = 101')
# Elimina todos los datos en la fila 101

try:
    conexion.commit()
    print("Cambios guardados exitosamente en la Base de Datos")
except:
    print("No se han podido guardar los cambios en la Base de Datos")
