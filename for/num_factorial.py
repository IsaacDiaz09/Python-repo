# Hallar el factorial de un número positivo.
factorial = 1

numero = int(input("Ingrese un número para hallar su factorial: "))

while numero < 0:
    print("Solo se admiten números positivos.")
    numero = int(input("Ingrese un número para hallar su factorial: "))

for i in range(1,numero+1,1):
    factorial *= i
print(f"El factorial de {numero} es {factorial}")
