# Escribir un programa que solicite al usuario una cantidad y luego
# itere la cantidad de veces dada. En cada iteración, solicitar al
# usuario que ingrese un número. Al finalizar, mostrar la suma de todos
# los números ingresados.
suma = 0
cantidad = int(input("Introduce la cantidad de números a ingresar: "))

for i in range(cantidad):
    numero = int(input(f"Introduce el valor {i+1} de {cantidad}: "))
    suma = suma + numero

print(f"\nLa sumatoria de los números ingresados es: {suma}")
