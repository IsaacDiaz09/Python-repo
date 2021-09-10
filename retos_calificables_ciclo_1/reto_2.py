# Reto 2: Multas por exceso de velocidad.

distancia, velocidad, tiempo = input().split()

tiempo = int(tiempo)
distancia = int(distancia)
velocidad = int(velocidad)

"""
print(type(distancia))
print(type(velocidad))
print(type(tiempo))"""


def multas_velocidad(distancia, velocidad, tiempo):
    vel_media = distancia / tiempo * 3.6
    vel_media_multa = velocidad + (velocidad*0.2)

    if tiempo > 0 and distancia > 0 and velocidad > 0:

        if vel_media < velocidad:
            return str("OK")

        elif vel_media > velocidad and vel_media_multa > vel_media:
            return str("MULTA")

        else:  # vel_media >= vel_media_multa:
            return str("CURSO SENSIBILIZACION")
    else:
        return str("ERROR")


print(multas_velocidad(distancia, velocidad, tiempo))
