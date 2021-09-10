dict_ocurrencias = {}
ocurrencias_notas = []
exms_copiados = 0
detecta_profesor = 0
repetidos = []
iguales = False
n, k = input().split()
n = int(n)
k = int(k)

respuestas = input()
respuestas_lista = [int(d) for d in respuestas.split()]
respuestas_lista.reverse()

for x in respuestas_lista:
    if x not in repetidos:
        repetidos.append(x)

for i in respuestas_lista:
    if i in dict_ocurrencias:
        dict_ocurrencias[i] += 1
    else:
        dict_ocurrencias[i] = 1

ocurrencias = dict_ocurrencias.values()

for num in ocurrencias:
    num = num-1
    ocurrencias_notas.append(num)
    exms_copiados += num


def final_list(respuestas_lista, k): return [
    respuestas_lista[i:i+k+1] for i in range(len(respuestas_lista)-k)]


resultado = final_list(respuestas_lista, k)


def f_repetidos_sublistas(resultado, repetidos):
    respuesta = 0
    for lista in resultado:
        for x in repetidos:
            if lista.count(x) >= 2:
                respuesta += lista.count(x) - 1
    return respuesta

if(all((i) == respuestas_lista[0] for i in respuestas_lista)):
    print(exms_copiados,exms_copiados)
else:
    print(exms_copiados, f_repetidos_sublistas(resultado, repetidos))
