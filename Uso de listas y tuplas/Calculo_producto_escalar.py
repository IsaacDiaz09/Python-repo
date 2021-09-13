print("Bienvenido al programa de calculo del Producto escalar entre \
dos vectores!")

x1, y1 = input("\nIntroduce el valor para  'x' y 'y' del vector 1: ")\
    .split(sep=",")

x2, y2 = input("\nIntroduce el valor para  'x' y 'y' del vector 2: ")\
    .split(sep=",")


def prod_escalar(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    resultado1 = x1 * x2
    resultado2 = y1 * y2

    producto_escalar = resultado1 + resultado2

    return f"\nEl Producto Escalar entre los vectores {x1,y1} y {x2,y2} es\
: {producto_escalar}"


print(prod_escalar(x1, y1, x2, y2))

print("Fin del programa")
