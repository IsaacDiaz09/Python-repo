#!/usr/local/bin/python
# coding: utf-8
def suma(num1, num2):  # Función de suma
	return num1+num2

def resta(num1, num2):   # Función de resta
	return num1-num2

def multiplica(num1, num2):   # Función de multiplicación
	return num1*num2

def divide(num1,num2):    # Función de división
	try:
		return num1/num2

	except ZeroDivisionError:
		print("No se puede dividir entre 0")   # Intente realizar la división, y si arroja error de 
		return "Operación erronea"             # 'ValueError' imprime el mensaje y sigue con la ejecución del 
		                                       # resto del código """

while True:       # Rechaza un valor que no sea 'int' en un bucle infinito, se puede realizar ->
	try:          # -> también de la forma que lo hice en el ejercicio 'baraja_francesa'
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break
	except ValueError:
		print("Los valores introducidos no son válidos, intente de nuevo.")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")