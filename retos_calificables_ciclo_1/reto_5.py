# DICCIONARIO PRODUCTOS.
imprimir = True
resultado = []
productos = {
    1: ["Manzanas", 5000, 25],
    2: ["Limones", 2300, 15],
    3: ["Peras", 2700, 33],
    4: ["Arandanos", 9300, 5],
    5: ["Tomates", 2100, 42],
    6: ["Fresas", 4100, 3],
    7: ["Helado", 4500, 41],
    8: ["Galletas", 500, 8],
    9: ["Chocolates", 3500, 80],
    10: ["Jamon", 15000, 10]
}

operacion = input()
codigo, nombre, precio, inventario = input().split()
codigo = int(codigo)
precio = int(precio)
inventario = int(inventario)

lista_prod = [nombre, precio, inventario]

if operacion == "AGREGAR":
    if codigo in productos:
        print("ERROR")
        imprimir = False
    else:
        def agregar_producto(codigo):
            productos[codigo] = lista_prod
            return productos

        agregar_producto(codigo)

if operacion == "ACTUALIZAR":
    if codigo not in productos:
        print("ERROR")
        imprimir = False
    else:
        def actualizar_producto(codigo):
            productos[codigo] = lista_prod
            return productos

        actualizar_producto(codigo)

if operacion == "BORRAR":
    if codigo not in productos:
        print("ERROR")
        imprimir = False
    else:
        def borrar_producto(codigo):
            del productos[codigo]
            return productos

        borrar_producto(codigo)

lista_precios = []
lista_productos = []
inventario = []

suma = 0

for i in list(productos.values()):
    lista_precios.append(i[1])
    suma += i[1]
    promedio = suma / len(lista_precios)
    inventario.append(i[2])

for i in list(productos.values()):
    suma += i[1]
    lista_productos.append(i[0])

posicion = lista_precios.index(max(lista_precios))
resultado.append(lista_productos[posicion])  # producto más caro

posicion = lista_precios.index(min(lista_precios))
resultado.append(lista_productos[posicion])  # producto más barato

val_total = 0

for i in range(0, len(lista_precios)):
    operacion = inventario[i] * lista_precios[i]
    val_total += operacion

resultado.append(float(round(promedio, 1)))
resultado.append(float(round(val_total, 1)))
if imprimir:
    print(resultado[0], resultado[1], resultado[2], resultado[3])
