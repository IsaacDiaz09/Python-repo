from math import sqrt
# La mas facil, haciendo uso de un metodo de la libreria math


# Se valida el numero de entrada
while True:
    try:
        numero = float(input("Introduce un número para hallar la raíz cuadrada: "))
        break
    except ValueError:
        print("No puede ingresar un valor que no sea un número")

print(round(sqrt(numero),4))