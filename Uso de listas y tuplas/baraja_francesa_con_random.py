import random


contador = 0
mi_mano = []
nums_carta = []

""" Elementos de la Baraja Francesa. Todas las cartas de: treboles,
corazones, diamantes y picas. """


Baraja_francesa = [
    "1 de Tréboles", "2 de Tréboles", "3 de Tréboles", "4 de Tréboles",
    "5 de Tréboles", "6 de Tréboles", "7 de Tréboles", "8 de Tréboles",
    "9 de Treboles", "10 de Tréboles", "1 de Diamantes",
    "2 de Diamantes", "3 de Diamantes", "4 de Diamantes",
    "5 de Diamantes", "6 de Diamantes", "7 de Diamantes",
    "8 de Diamantes", "9 de Diamantes", "10 de Diamantes",
    "1 de Corazones", "2 de Corazones", "3 de Corazones",
    "4 de Corazones", "5 de Corazones", "6 de Corazones",
    "7 de Corazones", "8 de Corazones", "9 de Corazones",
    "10 de Corazones", "1 de Picas", "2 de Picas", "3 de Picas",
    "4 de Picas", "5 de Picas", "6 de Picas", "7 de Picas",
    "8 de Picas", "9 de Picas", "10 de Picas", "J de Tréboles",
    "R de Tréboles", "K de Tréboles", "J de Picas", "R de Picas",
    "K de Picas", "J de Diamantes", "R de Diamantes", "K de Diamantes",
    "J de Corazones", "R de Corazones", "K de Corazones"
]

print("**Inicio del programa**")

print("\n### El programa aleatoriamente eligirá cinco cartas de la \
Baraja Francesa para usted ###")

while contador <= 4:
    carta = random.choice(Baraja_francesa)
    mi_mano.append(carta)
    Baraja_francesa.remove(carta)
    num_carta = carta[0:2]
    for i in carta:
        numero = carta.split(sep=" ")
    nums_carta.append(numero[0])
    contador += 1

print(f"\nSu mano es:\
\n{mi_mano}")

num1,num2,num3,num4,num5 = nums_carta

if num1 == num2 and num1 == num3 and num1 == num4 or num1 == num5:
    print("\nSus cartas forman un POKER")
else:
    print("\nSus cartas no forman un POKER")
