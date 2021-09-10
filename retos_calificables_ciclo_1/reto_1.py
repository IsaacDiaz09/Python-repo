# Reto 1: El salario de Camilo.

sal_base, h_extras, bonificacion = input().split()

sal_base = float(sal_base)
h_extras = int(h_extras)         # Conversión a datos 'int'
bonificacion = int(bonificacion)

# Operaciones.
if bonificacion == 1:
    bonificacion = sal_base * 0.05
else:
    bonificacion = 0

h_trabajo = sal_base / 192
val_h_extras = h_extras * (h_trabajo * 1.25)

sal_total = sal_base + val_h_extras + bonificacion

# Descuentos de ley.
salud = (sal_total * 0.035)
pension = (sal_total * 0.04)
compensacion = (sal_total * 0.01)
descuentos = salud + pension + compensacion
sal_final = sal_total - descuentos
print(round(sal_final, 1))
