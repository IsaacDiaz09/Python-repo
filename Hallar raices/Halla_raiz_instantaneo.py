# metodo 2
""" 
Halla la raiz de forma instantanea con una unica iteracion
"""
from timeit import default_timer
numero = int(input())
inicio = default_timer()
raiz = numero**(1/2)
print(round(raiz, 2),)
fin = default_timer()
print(round(fin-inicio,6),"s")
