# Escribir una función que reciba un vector y devuelva su norma.

import math

print("¡Bienvenido! Este programa cálcula la norma de un vector")

x1, y1 = input("\nIntroduce el valor para  'x' y 'y' del vector: ")\
    .split(sep=",")


def calcula_norma(x1, y1):

    x1 = int(x1)
    y1 = int(y1)

    resultado = x1**2 + y1**2
    norma = math.sqrt(resultado)
    return f"\nLa norma del vector {x1,y1} es {norma}"


print(calcula_norma(x1, y1))
