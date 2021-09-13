import sqlite3
from sqlite3 import Error

try:
    conexion = sqlite3.connect('db\my_database_2.db')
    print('Conectado exitosamente')
except Error:
    print(Error)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM empleados_empresa')

filas = cursor.fetchall()
for fila in filas:
    print(f"Seleccion del registro -> {fila}")
    print(fila[0],f"{fila[1]} {fila[2]} {fila[3]})")
# Aqui obtengo los dos datos que necesito para la app tkinter,


try:
    conexion.commit()
    print("\nCambios guardados exitosamente en la Base de Datos")
except:
    print("\nNo se han podido guardar los cambios en la Base de Datos")
