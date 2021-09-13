from timeit import default_timer
# metodo 1

"""
Se halla la raiz cuadrada de un numero por el metodo babilonico:
que consiste en hacer una analogia con la formula de un rectangulo;
tomando como base la mitad del numero y altura 2, hallando progresivamente
la media ambos lados se van acercando al mismo valor, cuando se consigue, se 
toma como la raiz y la funcion deja de iterar y entrega el resultado
(muy eficiente)
"""

# Se valida el numero de entrada
while True:
    try:
        numero = float(input("Introduce un número para hallar la raíz cuadrada: "))
        break
    except ValueError:
        print("No puede ingresar un valor que no sea un número")


def raiz_babilonica(numero):
    area = numero
    global iteraciones
    iteraciones = 0
    x = area/2
    
    while True:
        if x*x == numero:
            return x
        else:
            x_viejo = x
            x = (x+(numero/x)) /2
            iteraciones+=1
        if x_viejo == x:
            break
    return x

inicio = default_timer()
print(round(raiz_babilonica(numero),3))
fin = default_timer()
print(f"Tiempo -> {round(fin-inicio,6)} ms")
print("iteraciones",iteraciones)