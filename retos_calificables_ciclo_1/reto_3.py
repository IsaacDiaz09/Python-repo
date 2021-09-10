# Reto 3: Selección de vivienda.

precios = []
disponibilidad = []

n = int(input())

for i in range(1, n+1):
    baños, habitaciones, tiempo, parques, precio = input().split()

    baños = int(baños)
    habitaciones = int(habitaciones)
    tiempo = int(tiempo)
    parques = int(parques)
    precio = int(precio)

    if baños >= 3 and habitaciones >= 4 and tiempo <= 35 and parques \
            >= 4:

        # precio = str(precio)
        precios.append(precio)
    else:
        disponibilidad.append("NO DISPONIBLE")


if len(precios) != 0:
    print(precios[0])

else:
    if len(disponibilidad) != 0:
        print(disponibilidad[0])
