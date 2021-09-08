# Encapsulación de propiedades y declarar un constructor, crear una segunda
# instancia a partir de la misma clase

# Clase coche
class Coche:
    # Definición de sus propiedades y estado inicial
    def __init__(self):
        self.largo_Chasis = 250
        self.ancho_Chasis = 120
        # self.ruedas = 4
        self.__ruedas = 4
        self.en_marcha = False
    # Definición de los comportamientos

    def arrancar(self,arranca):
        self.en_marcha = arranca
        if (self.en_marcha):
            return "El coche está en marcha."
        else:
            return "El coche está detenido."
        
    def estado(self):
        return f"El coche tiene {self.__ruedas} ruedas, un largo de \
{self.largo_Chasis} y un ancho de {self.ancho_Chasis}"

miCoche = Coche() # Instancia

print("Mi coche")
# Consulta de las propiedades
print(miCoche.estado())
# Arranca el coche ↓ recibiendo un argumento booleano
print(miCoche.arrancar(True))
# Ahora también nos indica su estado respecto a lo que se le paso
#######################

print("------ Creacion del segundo objeto ------")

print("Mi coche 2")
miCoche_2 = Coche()
# Consulta de las propiedades
miCoche_2.__ruedas = 7
print(miCoche_2.estado())
# dice que tiene 4 ruedas, la propiedad no ha cambiado
# 250 y 4 ruedas
print(miCoche_2.arrancar(False))
# Lo mismo aqui, se le pasa el argumento y dice si esta detenido o no
