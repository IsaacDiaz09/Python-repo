from timeit import default_timer

def busca_en_archivo(nombre_archivo, palabra_buscar):
    with open(f'D:/ESTUDIO/python/Persistencia de datos/julio_8_persistencia/txt/{nombre_archivo}', 
    'r', encoding="utf8") as myFile:
        lineas = myFile.readlines()
        texto_archivo = []

        for linea in lineas:
            texto_archivo.append(linea.split())
        
        def busca_palabra():
            for i in texto_archivo:
                if palabra_buscar in i:
                    return True
        
        if busca_palabra():
            print(f"\nLa palabra '{palabra_buscar}' se encuentra en el archivo actual")
        else:
            print(f"La palabra '{palabra_buscar}' no se encuentra en el archivo actual")

        print("\n --- El archivo se ha leído por completo --- ")


if __name__ == '__main__':
    inicio_1 = default_timer()
    busca_en_archivo("ejercicio_2.txt","oportunidad")
    fin_1 = default_timer()
    print(f"\nEl tiempo que tardó la ejecución fue de {round(fin_1-inicio_1,5)} s")
