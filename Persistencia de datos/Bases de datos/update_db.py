import sqlite3
from sqlite3 import Error

try:
    conexion = sqlite3.connect('db\my_database_0.db')
    print('Conectado exitosamente')
except Error:
    print(Error)

cursor = conexion.cursor()

dato1 = int(input("Inserte el dato de -> identificacion: "))
dato2 = input("Inserte el dato de -> Nombre: ")
dato3 = float(input("Inserte el dato de -> salario: "))

cursor.execute(f'UPDATE empleados_empresa SET Nombre = "{dato2}",salario = "{dato3}"\
where identificacion = {dato1}')

try:
    conexion.commit()
    print("Cambios guardados exitosamente en la Base de Datos")
except:
    print("No se han podido guardar los cambios en la Base de Datos")
