print("¡Bienvenido! Este programa le hará saber si dos vectores son \
paralelos o no")

x1, y1 = input("\nIntroduce el valor para  'x' y 'y' del vector 1: ")\
    .split(sep=",")

x2, y2 = input("\nIntroduce el valor para  'x' y 'y' del vector 2: ")\
    .split(sep=",")


def vectores_paralelos(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    resultado1 = x1 / x2
    resultado2 = y1 / y2

    if resultado1 == resultado2:
        print("\n************************************************")
        return f"Los vectores {x1,y1} y {x2,y2} son paralelos."

    else:
        print("\n************************************************")
        return f"Los vectores {x1,y1} y {x2,y2} no son paralelos."


print(vectores_paralelos(x1, y1, x2, y2))
