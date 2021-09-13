# Ejercicio 2.

""" Modifique el algoritmo del problema anterior para que, en vez de
comprobar que el número sea menor que 10, compruebe que se encuentre en
el rango (0,20) """

print("Inicio del programa. Bienvenido")

numero = int(input("Ingrese un número por favor: "))
while numero < 0 or numero > 20:
    numero = int(input("Ingreso un número no válido, pruebe de nuevo: "))
if 0 < numero < 20:
    print("El número ingresado es", numero)

print("Fin del programa")
