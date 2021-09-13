# Ejercicio 1.

""" Escriba un programa que capture un número entero y que compruebe si 
el número es menor que 10. Si no lo es, debe volver a capturar el número 
repitiendo la operación hasta que el usuario escriba el valor correcto. 
Finalmente, debe escribir por pantalla el valor leído cuando este sea 
correcto """

print("Inicio del programa. Bienvenido")

numero = int(input("Ingrese un número por favor: "))
while numero < 10:
    numero = int(input("Ingrese un número por favor: "))
if numero == 10:
    print("El número ingresado es", numero)

print("Fin del programa")
