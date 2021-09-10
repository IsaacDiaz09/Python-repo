# Escribir un programa que permita al usuario ingresar 6 números enteros
# que pueden ser positivos o negativos. Al finalizar, mostrar la
# sumatoria de los números negativos y el promedio de los positivos

lista_negativos = []
lista_positivos = []
suma = 0
suma2 = 0
contador = 0

for i in range(6):
    numero = int(input(f"Ingrese el valor {i+1} de 6 por favor: "))
    while numero == 0:
        print("No se puede introducir 0")
        numero = int(input("Ingrese un número por favor: "))
    if numero > 0:
        suma += numero
        contador += 1
        lista_positivos.append(numero)
    if numero < 0:
        suma2 += numero
        lista_negativos.append(numero)
    else:
        promedio = suma/contador

print(lista_positivos)
print(lista_negativos)
print(f"La sumatoria de los numeros negativos es: {suma2}")
print(f"El promedio de los números positivos es de: {round(promedio,1)}")
