# Solicita al usuario que ingrese una frase y luego imprimir la cantidad
# de vocales que tiene dicha frase.

frase = input("Ingrese una frase: ")
vocales = "a,e,i,o,u,A,I,O,U,E"
contador = 0

for i in frase:
    if i in vocales:
        contador += 1
        print(contador)

print(f"La frase ingresada: {frase} tiene {contador} vocal(es)")
