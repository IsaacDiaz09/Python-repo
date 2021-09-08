from constantes import Numeros

"""
Si se intenta reasignar el valor de una constante arroja: AttributeError: Cannot reassign members.
"""
Numeros.NUM_E = 20

# Muestra de los tipos e info en pantalla

numero_pi = Numeros.NUM_PI
print(numero_pi)
print(type(numero_pi))
print(numero_pi.value)
# Muestra de los tipos e info en pantalla

numero_e = Numeros.NUM_E
print(numero_e)
print(type(numero_e))
print(numero_e.value)
