# Ejercicio 9
""" Escribir un programa que pida al usuario una palabra y muestre por 
pantalla el número de veces que contiene cada vocal """
from operator import itemgetter

num = 0
vocales = ["a", "e", "i", "o", "u"]
diccionario = {}

frase = input("Ingrese una frase para realizar el conteo de vocales: ")
frase = frase.lower()

for i in frase:
    if i in vocales:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
# del diccionario[' ']  # Elimina los espacios en blanco.
diccionario_ordenado = sorted(diccionario.items(), key=itemgetter(0))

print(diccionario)
print(dict(diccionario_ordenado))
