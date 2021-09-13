# Ejercicio 5.

monto = int(input("Ingrese el valor del monto de su compra, 0 para cancelar: "))
suma = 0
descuento = 1

print("Inicio del programa")

while monto != 0:
    if monto < 0:
        monto = int(
            input("Ingrese el valor del monto de su compra, 0 para cancelar: "))
        print(suma)
    else:
        suma = monto + suma
        monto = int(
            input("Ingrese el valor del monto de su compra, 0 para cancelar: "))
        print(suma)

if suma > 1000:
    descuento = 0.1
    valor_final = suma - (suma*descuento)
    print("Su valor a pagar con descuento del '10% es:", valor_final)
else:
    valor_final = suma * descuento
    print("Su valor a pagar  es:", valor_final)

print("Fin del programa")
