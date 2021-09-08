# Superclase ↓
class Animales():
    def __init__(self,animal,alimento,altura,color,habitat):
        self.__animal = animal
        self.patas = 4
        self.__alimentacion = alimento
        self.__altura = altura
        self.__color = color
        self.__habitat = habitat
        self.__duerme = False

    def dormido(self,duerme):
        self.__duerme = duerme
        if self.__duerme:
            return "Está durmiendo..."
        else:
            return "Está despierto"
    
    def descripcion(self):
        print(f"--Descripcion Animal--\nAnimal: {self.__animal}\nPatas: \
{self.patas}\nSe alimenta de: {self.__alimentacion}\nAltura: \
{self.__altura}m\nColor: {self.__color}\nHabitat: {self.__habitat}")


print()
print("---Primer instancia (de superclase)---")
mono = Animales("Mono","Frutas y semillas","1.5","Café","Jungla")
mono.descripcion()
print("¿Duerme?",mono.dormido(True))
print()

class aves(Animales):
    def descripcion(self):
        self.patas = 2
        self.ave_vula = False
        super().descripcion()
    def vuela(self,volar):
        self.ave_vuela = volar
        if self.ave_vuela:
            return "El ave esta volando"
        else:
            return "El ave no esta volando ahora"

print("--- Instancia de Subclase ---")
colibri = aves("Colíbri","Semillas","0.1","Amarillo","Nidos en árboles")
colibri.descripcion()
print("Volar:",colibri.vuela(True))
print()

##########################################

class animal_2_patas:
    def __init__(self,nombre,color,peso):
        self.nombre = nombre
        self.color = color
        self.peso = peso
        self.__patas = 2
    def descripcion(self):
        print(f"Nombre: {self.nombre}\nColor: {self.color}\nPeso: \
{self.peso}Kg\nPatas: {self.__patas}")

print("-- PATO --")
pato = animal_2_patas("Pato","Blanco",8)
pato.descripcion()


class carnivoro:
    def __init__(self):
        self.Alimentacion = "Carne y carroña"

class aguila(animal_2_patas,carnivoro):
    def descripcion(self):
        carnivoro.__init__(self) # Se debe especificar qué clase heredada
        super().descripcion()    # y qué importar para evitar sobre-escribirlo
        print("Alimentación:", self.Alimentacion)

print("\n__ Objeto Aguila __")
pepe = aguila("Pepe","Blanco con negro",18)
pepe.descripcion()
print()
