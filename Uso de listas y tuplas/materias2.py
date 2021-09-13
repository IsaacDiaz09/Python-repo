# Ejercicio 2:
""" Escribir un programa que almacene las asignaturas de un curso (por 
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
la muestre por pantalla el mensaje Yo estudio <asignatura>, donde 
<asignatura> es cada una de las asignaturas de la lista """

num = 0

materias = ["Matemáticas", "Sociales", "Naturales", "Artes", "Historia"]

while num <= 4:
    print(f"Yo estudio: {materias[num]}")
    num += 1
