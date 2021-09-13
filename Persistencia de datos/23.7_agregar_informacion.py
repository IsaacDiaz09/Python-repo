with open("txt/agregando_data.txt","w") as file:
    cantidad_numeros = int(input("Digite la cantidad de numeros que quiere guardar"))
    for numero in range(cantidad_numeros):
        dato = input("Digitite el numero que sea guardar: ")
        file.write(dato + ",")