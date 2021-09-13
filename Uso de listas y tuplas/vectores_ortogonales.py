""" Escribir una función que reciba dos vectores y devuelva si son paralelos
o no """

print("¡Bienvenido! Este programa le hará saber si dos vectores son \
ortogonales o no")

x1, y1 = input("\nIntroduce el valor para  'x' y 'y' del vector 1: ")\
    .split(sep=",")

x2, y2 = input("\nIntroduce el valor para  'x' y 'y' del vector 2: ")\
    .split(sep=",")


def vector_ortogonal(x1, y1, x2, y2):

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    resultado = (x1*x2) + (y1*y2)

    if resultado == 0:
        print("\n**************************************************")
        return (f"Los vectores {x1,y1} y {x2,y2} son ortogonales.")
    else:
        print("\n**************************************************")
        return f"Los vectores {x1,y1} y {x2,y2} no son ortogonales."


print(vector_ortogonal(x1, y1, x2, y2))
