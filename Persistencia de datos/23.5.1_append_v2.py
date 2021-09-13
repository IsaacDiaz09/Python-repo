palabras = ["hola", "como", "estan", "ya", "casi", "son", "expertos", "en", "python"]

with open ("txt/reporte2.txt", "a") as archivo:
    for palabra in palabras:
        archivo.write(palabra + "\n")