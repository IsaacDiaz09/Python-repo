# Ejercicio 7:
""" Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones múltiplos de 3, y
muestre por pantalla la lista resultante """

letras_multiplos_3 = []

abecedario = [
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", 
"ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            ]
for i in abecedario:
    if abecedario.index(i) % 3 == 0:
        letras_multiplos_3.append(i)
print(f"Letras del abecedario cuyo indice en lista es múltiplo de 3: \
{letras_multiplos_3}")

"""text2 = ["a","b","c"]
for i in text2:
	print(text2.index(i))"""
