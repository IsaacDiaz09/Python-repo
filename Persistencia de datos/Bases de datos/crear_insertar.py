import sqlite3

try:
    conexion = sqlite3.connect('db\my_database_0.db')
    print('Conectado exitosamente')
except:
    print('No se pudo conectar con la base de datos')

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE empleados_empresa(identificacion integer PRIMARY KEY, \
# Nombre text, salario real)")
# -> Se comenta por que ya se creó la tabla, daria un error ejecutarlo de nuevo

print()
dato1 = int(input("Ingrese el dato de -> identificacion: "))
dato2 = input("Ingrese el dato de -> nombre: ")
dato3 = float(input("Ingrese el dato de -> salario: "))

cursor.execute("INSERT INTO empleados_empresa (identificacion,Nombre, salario) \
VALUES(?,?,?);", (dato1,dato2,dato3))

cursor.execute("INSERT INTO empleados_empresa (identificacion,Nombre, salario) \
VALUES(?,?,?);", (dato1+1,dato2+"d2",dato3))

cursor.execute("INSERT INTO empleados_empresa (identificacion,Nombre, salario) \
VALUES(?,?,?);", (dato1+2,dato2+"d3",dato3))

try:
    conexion.commit()
    print("Cambios guardados exitosamente en la Base de Datos")
except:
    print("No se han podido guardar los cambios en la Base de Datos")
