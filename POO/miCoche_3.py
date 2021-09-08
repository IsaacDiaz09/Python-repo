# Encapsulando ahora métodos

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
        # Si el coche recibe la orden de arrancar , entonces realiza el 
        # chequeo, y, si el chequeo fue exitoso, enciende el coche 
        self.en_marcha = arranca
        if (self.en_marcha):
            chequeo = self.__chequeo_miCoche()
            
        if (self.en_marcha and chequeo):
            return "El coche está en marcha."
        elif (self.en_marcha and chequeo == False):
            # Si recibio la orden de arrancar y ha salido mal el chequeo, mi
            # coche no enciende
            return "El sistema ha detectado un problema en el chequeo inicial.\
 No puede arancar el coche"
        else:
            return "El coche está detenido."
        
    def estado(self):
        return f"El coche tiene {self.__ruedas} ruedas, un largo de \
{self.largo_Chasis} y un ancho de {self.ancho_Chasis}"

    def __chequeo_miCoche(self):
        print("Realizando chequeo interno del coche...")
        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas ==\
        "cerradas"):
            return True
        else:
            return False


miCoche = Coche() # Instancia

print("Mi coche")
# Consulta de las propiedades
print(miCoche.estado())
# Arranca el coche ↓ recibiendo un argumento booleano
print(miCoche.arrancar(True))
# Ahora también nos indica su estado respecto a lo que se le paso

print("-------Creacion del segundo objeto-------")

print("Mi coche 2")
miCoche_2 = Coche()
# Consulta de las propiedades
miCoche_2.__ruedas = 7
print(miCoche_2.estado())
# dice que tiene 4 ruedas, la propiedad no ha cambiado
# 250 y 4 ruedas
print(miCoche_2.arrancar(False)) 
# Lo mismo aqui, se le pasa el argumento y dice si esta detenido o no

# No realiza el chequeo porque no se le dio la instruccion de arrancar
