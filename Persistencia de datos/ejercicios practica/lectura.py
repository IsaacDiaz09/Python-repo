info_txt = []
with open("txt/texto_1.txt","r") as archivo:
    lineas = archivo.read()
    for linea in lineas:
        print(linea, end= "")
        info_txt.append(linea)
    """print(lineas)"""

print("\n")

print("".join(info_txt))
