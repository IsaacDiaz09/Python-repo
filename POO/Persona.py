class Persona():
    def __init__(self,nombre,apellido,cedula,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.sexo = sexo
    
    def hablar(self, mensaje):
        return mensaje
    
    def obtener_sexo(self, sexo):
        sexo = sexo.upper()
        if sexo == "M":
            return "Masculino"
        elif sexo == "F":
            return "Femenino"
        else:
            return "¿¿??"
    def descripcion(self):
        return f"Nombre: {self.nombre}\nApellido(s): {self.apellido}\nCédula: \
{self.cedula}\nSexo: {self.obtener_sexo(self.sexo)}"

print()
print("-- Persona --")
Paola = Persona("Paola","Muñoz",1119323465,"F")
print(Paola.descripcion())
print()

class Supervisor(Persona):
    def __init__(self, nombre, apellido, cedula, sexo,supervisa):
        super().__init__(nombre, apellido, cedula, sexo)
        self.supervisa = supervisa
        self.tareas = ["Revisar arena", "Gestionar horarios trabajadores",
"Traer material", "Generar reportes"]

    def imprime_tareas(self):
        print("\n-Tareas:")
        for i in self.tareas:
            print(i)
    
    def supervisando(self):
        if self.supervisa:
            return f"Vuelve al trabajo {Paola.nombre}!!!"
        else:
            return "Todo va bien por el momento"
    def descripcion(self):
        return super().descripcion() + f"\nSupervisando: {self.supervisa}"

print("-- Supervisor --")
Raul = Supervisor("Raul", "Colmenares", 1174598632, "M",True)
print(Raul.descripcion())
print(Raul.supervisando())
Raul.imprime_tareas()
print()

print("mro de la clase Supervisor:",Supervisor.__mro__)
