# Ejercicio 4.

""" Escriba un programa que sume los números ingresados por el usuario y 
cuando la suma sea superior a 100 deje de pedir números y muestre el
total"""

suma = 0
while suma <= 100:
	numero = int(input("Ingrese un número: "))
	suma = numero + suma

print("La sumatoria de los números ingresados es:",suma)
