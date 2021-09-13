# Ejercicio 3:
""" Escribir un programa que almacene las asignaturas de un curso (por 
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después 
las muestre por pantalla con el mensaje En <asignatura> has sacado 
<nota> donde <asignatura> es cada una de las asignaturas de la lista y 
<nota> cada una de las correspondientes notas introducidas por el 
usuario """

num = 0
notas_lista = []

materias = ["Matemáticas", "Sociales", "Naturales", "Artes", "Historia"]

while num <= 4:
    nota = float(input(f"¿Cuál ha sido su calificación en \
{materias[num]}?: "))
    num += 1
    notas_lista.append(nota)

print("**********************************************")

num = 0
while num <= 4:
    print(f"Su calificación en {materias[num]} fue de: \
{notas_lista[num]}")
    num += 1
