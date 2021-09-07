import re
"""
El programa leerá n lineas e ira mostrando los resultados de cada evaluacion.
(si es aceptada o no como contraseña siguiento unas reglas)
Se detendra cuando reciba la palabra 'end'
"""
# al menos una vocal [aeiou]+
# no 3 vocales consecutivas [aeiou]{3}
# no 3 consonantes consecutivas [bcdfg...z]{3}
# no 2 misma letra consecutiva excepto 'ee' u 'oo' a{2}b{2}c{2}d{2}...
salida = ""
while True:
    pswd = input()
    if pswd == "end":
        break
    else:
        # Confirma si tiene alguna vocal, si es asi, pasa al siguiente filtro
        pattern = re.compile(r"[aeiou]+", re.IGNORECASE)
        match = pattern.search(pswd)

        if match:
            pattern = re.compile(
                r"[aeiou]{3}|[bcdfghjklmnñpqrstvwxyz]{3}|a{2}|b{2}|c{2}|d{2}|e{3}|f{2}|g{2}|h{2}|i{2}|j{2}|k{2}|l{2}|m{2}|n{2}|ñ{2}|o{3}|p{2}|q{2}|r{2}|s{2}|t{2}|u{2}|v{2}|w{2}|x{2}|y{2}z{2}", re.IGNORECASE)
            match = pattern.search(pswd)

            if match is None:
                salida += "<{}> is acceptable.\n".format(pswd)
            else:
                salida +="<{}> is not acceptable.\n".format(pswd)
        else:
            salida += "<{}> is not acceptable.\n".format(pswd)
print(salida)

"""
Entradas:

abc
tv
  
hey!
mypassword
ttttttvvvvv
super
sssuper
suppppeeeier
hii
oops
end


Salidas:

<abc> is acceptable.
<tv> is not acceptable.
<  > is not acceptable.
<hey!> is acceptable.
<mypassword> is not acceptable.
<ttttttvvvvv> is not acceptable.
<super> is acceptable.
<sssuper> is not acceptable.
<suppppeeeier> is not acceptable.
<hii> is not acceptable.
<oops> is acceptable.
"""