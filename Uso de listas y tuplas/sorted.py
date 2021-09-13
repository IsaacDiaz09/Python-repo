# Ejercicio 4:
""" Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista y los muestre por
pantalla ordenados de menor a mayor """

num1, num2, num3, num4, num5 = input("Ingrese los números ganadores\
 de la 'Loteria primitiva' seguidos de un espacio(son 5 pares de \
números): ").split()

numeros_ganadores = [num1, num2, num3, num4, num5]

numeros_ordenados = sorted(numeros_ganadores)

print(f"Números desordenados: {numeros_ganadores}")

print(f"Números ordenados: {numeros_ordenados}")
