# Ejercicio 6:
""" Escribir un programa que almacene las asignaturas de un curso (por 
ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
por pantalla las asignaturas que el usuario tiene que repetir """

num = 0
materias_reprobadas = []

materias = ["Matemáticas", "Sociales", "Naturales", "Artes", "Historia"]
print(f"La nota mínima para aprobar una asignatura es de 7 (sobre 10)\n\
Asignaturas: {materias}")


while num <4:
    nota = float(input(f"¿Cúal fue su calificación en {materias[num]}\
?: "))
    num += 1
    if nota >= 7:
        materias_reprobadas.append(materias[num])

print("**********************************************")

if len(materias_reprobadas) == 0:
    print("El estudiante no debe repetir ninguna materia ¡Felicidades!")
else:
    print(f"El estudiante debe repetir: {materias_reprobadas}")
