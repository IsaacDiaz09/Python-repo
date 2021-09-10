# Escribir un programa que permita al usuario ingresar dos años y
# luego imprima todos los años en ese rango, que sean bisiestos y
# múltiplos de 10.
# Nota: para que un año sea bisiesto debe ser divisible por 4 y no
# debe ser divisible por 100, excepto que también sea divisible por
# 400.

year_1 = int(input("Ingrese un año inicial: "))
year_2 = int(input("Ingrese un año final: "))
anos_bisiestos = []
anos_multiplos10 = []

while year_2 < year_1:
    print("El año final no puede ser inferior al inicial.")
    year_2 = int(input("Ingrese un año final: "))

for i in range(year_1, year_2):
    if i % 4 == 0:
        anos_bisiestos.append(i)
print("Los años bisiestos en el rango ingresado son:",
      anos_bisiestos)

for i in range(year_1, year_2):
    if i % 10 == 0:
        anos_multiplos10.append(i)
print("Los años que son múltiplos de 10 del rango ingresado son:",
      anos_multiplos10)
