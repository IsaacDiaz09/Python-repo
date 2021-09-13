from timeit import default_timer

def enumera_lineas(nombre_archivo):
    with open(f'D:/ESTUDIO/python/Persistencia de datos/julio_8_persistencia/txt/{nombre_archivo}', 'r',encoding="utf8") as myFile:
        lineas = myFile.readlines()
        n_lin = 0

        for linea in lineas:
            n_lin +=1
            print(f"Línea {n_lin} -> {linea}")

        print("\n --- El archivo se ha leído por completo --- ")


inicio_1 = default_timer()
enumera_lineas("ejercicio_2.txt")
fin_1 = default_timer()

print(f"\nEl tiempo que tardó la ejecución fue de {round(fin_1-inicio_1,5)} s")
