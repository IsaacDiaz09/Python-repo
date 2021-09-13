# Ejercicio 5:
""" Escribir un programa que almacene en una lista los números del 1 al 
10 y los muestre por pantalla en orden inverso separados por comas """

lista_ordenada = []
lista_reverso = []

for i in range(1, 11):
    lista_ordenada.append(i)

for i in reversed(lista_ordenada):
    lista_reverso.append(i)

print(lista_ordenada)
print(lista_reverso)
