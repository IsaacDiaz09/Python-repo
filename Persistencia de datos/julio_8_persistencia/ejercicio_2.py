from timeit import default_timer
# Metodo comun
inicio_1 = default_timer()
with open('D:/ESTUDIO/python/Persistencia de datos/julio_8_persistencia/txt/\
ejercicio_2.txt', 'r',encoding="utf8") as myFile:

    contador = 0
    lineas = myFile.readlines()
    for linea in lineas:
        for caracter in linea:
            contador += 1

    print("\n --- El archivo se ha leído por completo --- ")
    print(f"\nEl archivo de texto tiene {contador} carácteres\n")
fin_1 = default_timer()

# Ahora usando listas

inicio_2 = default_timer()
with open('D:/ESTUDIO/python/Persistencia de datos/julio_8_persistencia/txt/\
ejercicio_2.txt', 'r',encoding="utf8") as myFile2:

    texto = []

    contador_2 = 0
    lineas = myFile2.readlines()
    for linea in lineas:
        for caracter in linea:
            texto.append(caracter)


    print("\n --- El archivo se ha leído por completo --- ")
    print(f"\nEl archivo de texto tiene {len(texto)} carácteres")
fin_2 = default_timer()

# Medimos la eficiencia de ambos programas
print()
print(f"El tiempo que tardó la primera ejecución fue de {round(fin_1-inicio_1,5)} s")
print(f"El tiempo que tardó la segunda ejecución fue de {round(fin_2-inicio_2,5)} s")
