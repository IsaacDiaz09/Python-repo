# https://www.codechef.com/problems/KTTABLE

"""
Entrada: 
2 -> Casos de prueba
3 -> Numero de estudiantes
1 10 15 -> momentos terminar de cocinar
1 10 3 -> tiempo requerido cocinar
3
10 20 30
15 5 20

Salida: 
2 -> pudieron cocinar
1 -> pudo cocinar
"""

tests = int(input())
for _ in range(tests):
    cont = 0
    e = int(input())
    
    momentosTerminar = [int(i) for i in input().split()] 
    tiempoRequerido = [int(j) for j in input().split()]
    
    tiempo = momentosTerminar[0]
    
    if (tiempo - tiempoRequerido[0]) >= 0:
        cont += 1
        
    for i in range(1,e):
        tiempo = momentosTerminar[i] - momentosTerminar[i-1]
        if (tiempo - tiempoRequerido[i]) >= 0:
            cont += 1
    print(cont)
