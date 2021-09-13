# Ejercicio:
""" Crea un programa que pida al usuario un número real y muestra su 
raíz cuarta (la raíz cuadrada de la raíz cuadrada)"""
from math import sqrt

numero = int(input("Ingrese un número: "))

def mi_funcion(numero):
    resultado = sqrt(sqrt(numero))
    return f"La raíz cuarta de {numero} es {round(resultado,4)}"

print(mi_funcion(numero))