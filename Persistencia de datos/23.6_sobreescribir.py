palabras = ["hola", "como", "estan", "ya", "casi", "son", "expertos", "en", "python"]
contador = 1

with open("txt/reporte2.txt", "w") as archivo:
    for palabra in palabras:
        archivo.write(f"{contador} {palabra}\n")
        contador += 1