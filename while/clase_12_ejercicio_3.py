# Ejercicio 3.

""" Escriba un programa que sume los números ingresados por el usuario 
hasta que se ingrese el número 0 """

print("Inicio del programa. Bienvenido")
suma = 0
numero = int(input("Ingrese un número a sumar, 0 para finalizar: "))

while numero != 0:
    if numero > 0:
        suma = suma + numero
        numero = int(input("Ingrese un número a sumar: "))


print("La sumatoria de los números ingresados es", suma)

print("Fin del programa")
