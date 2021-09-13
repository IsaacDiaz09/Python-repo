# Ejercicio 8:
""" Escribir un programa que pida al usuario una palabra y muestre por 
pantalla si es un palíndromo """
# Los palíndromos son palabras que se leen igual al derecho y al revés.

palabra_reves = []
palabra = input("Introduce una palabra para verificar si es un \
palindromo: ").lower()

palabra_lista = list(palabra)

for i in reversed(palabra):
    palabra_reves.append(i)

if palabra_lista == palabra_reves:
    print(f"La palabra '{palabra}' es palíndroma.")
else:
    print(f"La palabra '{palabra}' no es palíndroma")
print()
