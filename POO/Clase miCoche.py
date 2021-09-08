# Creación de la clase y establecimiento de un par de atributos y métodos,
# también consulta de los mismos

# Clase coche
class Coche:
    # Definición de sus propiedades
    largo_Chasis = 250
    ancho_Chasis = 120
    ruedas = 4
    en_marcha = False

    # Definición de los comportamientos
    def arrancar(self):
        self.en_marcha = True

    def estado(self):
        if (self.en_marcha):
            return "El coche está en marcha."
        else:
            return "El coche está detenido."


miCoche = Coche() # Instancia
# Consulta de las propiedades
print(f"El largo del chasis de mi coche es: {miCoche.largo_Chasis}")
print(f"Mi coche tiene: {miCoche.ruedas} ruedas")
# Arranca el coche ↓
miCoche.arrancar()
# Saber si el coche esta parado o en marcha
print(miCoche.estado())
