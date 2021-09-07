# Documentación: https://docs.python.org/es/3/howto/regex.html#:~:text=Las%20expresiones%20regulares%20(llamadas%20RE,a%20trav%C3%A9s%20del%20m%C3%B3dulo%20re%20.
import re
str = "cadena"
# El patron define un rango de las vocales que debe encontrar almenos una vez
print(re.search(r"[aeiou]+",str))
# <re.Match object; span=(1, 2), match='a'> = Encontró la coincidencia

# ////////////////////////// Validar fecha \\\\\\\\\\\\\\\\\\\\\\\\\\

# Expresionn 1
fecha = "31/02/2011"
"""
Patron que verifica solo el formato de fecha dd/mm/aaaa
"""
validacion1 = re.compile(r"\d\d/\d\d/\d\d\d\d")
resultado = validacion1.search(fecha)

if resultado:
    print("Es una fecha válida")
else:
    print("No es una fecha válida")
# dice que es una fecha valida pero es incorrecto. Febrero max tiene 29 dias

# Expresion 2
"""
Patron que valida todo lo necesario excepto la cantidad max de dias segun el mes y si el año es bisiesto o no
"""
validacion2 = re.compile(r"^(0?[1-9]|[12][0-9]|3[01])/0?[12]|1[012]/((19|20)\d\d)$")
resultado = validacion2.search(fecha)

if resultado:
    print("Es una fecha válida")
else:
    print("No es una fecha válida")
# Cumple el patron y dice que es valida pues sigue ignorando lo de los dias de febrero


# Expresion 3 (Pendiente)
validacion3 = re.compile(r"")
resultado = validacion3.search(fecha)

if resultado:
    print("Es una fecha válida")
else:
    print("No es una fecha válida")
