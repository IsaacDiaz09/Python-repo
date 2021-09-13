""" 
Halla la raíz cuadrada de un número haciendo numerosas iteraciones en 
las que suma pequeños valores y comprueba si n*n es el numero que ingreso 
el usuario, de ser asi, se ha hallado la raíz (no muy eficiente)
"""
from timeit import default_timer
# metodo 1
while True:
    try:
        numero = float(input("Introduce un número para hallar la raíz cuadrada: "))
        break
    except ValueError:
        print("No puede ingresar un valor que no sea un número")

def halla_raiz_cuadrada():
    iteraciones = 0
    num = 0
    while num*num <= numero:
        num += 0.001
        iteraciones += 1
    return f"{round(num,2)}, iteraciones: {iteraciones}"

print()
inicio = default_timer()
print(halla_raiz_cuadrada())
fin = default_timer()
print(round(fin-inicio,6),"s")