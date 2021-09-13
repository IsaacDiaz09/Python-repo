contador = 1

with open("C:/Users/Camilo/Desktop/reportes/reporte2.txt","r") as archivo:
    data = archivo.readlines()

print("El archivo tiene",len(data), "lineas")

for linea in data:
    print(f"En la linea {contador} esta es la informacion: {linea}", end="")
    print()
    contador+=1