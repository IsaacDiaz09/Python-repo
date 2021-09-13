with open("C:/Users/Camilo/Desktop/reportes/reporte2.txt","r") as archivo:
    data = archivo.readlines()
    print(data)
    for frase in data:
        print("Esta es la cantidad de caracteres que hay en esta linea",len(frase))
        print(frase, end="")