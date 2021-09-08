# POO VIII
# Funciones 'super()' e 'isinstance()'

class Persona:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print(f"Nombre {self.nombre}\nEdad: {self.edad}\nLugar de residencia: \
{self.lugar_residencia}")
""" Declaración de clase que define a una persona con las propiedades: nombre,
edad y lugar de residencia """


class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        # Valores fijos ↓-↓
        super().__init__("Juan", 55, "Costa Rica")
        # La función super llama al método padre (Persona) y le pasa los 
        # Argumentos que solicita ya que son diferentes a los del inicializador
        # de 'Empleado', caso contrario, dará error 'AttributeError'.
        self.salario = salario
        self.antiguedad = antiguedad

Juan = Empleado(1200,2)
print()
print("--- Persona Juan ---")
Juan.descripcion()
print()

# Parte 2:

class Persona_2:
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):
        print(f"Nombre {self.nombre}\nEdad: {self.edad}\nLugar de residencia: \
{self.lugar_residencia}")
""" Declaración de clase que define a una persona con las propiedades: nombre,
edad y lugar de residencia """

class Empleado_2(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado,
    residencia_empleado):
        # Valores ya no fijos ↓-↓, variables
        super().__init__(nombre_empleado, edad_empleado,residencia_empleado)
        # La función super llama al método padre (Persona) y le pasa los 
        # Argumentos que solicita ya que son diferentes a los del inicializador
        # de 'Empleado', caso contrario, dará error 'AttributeError'.
        self.salario = salario
        self.antiguedad = antiguedad
    # Opcion 1 ↓
    """def descripcion(self):
        print(f"Nombre {self.nombre}\nEdad: {self.edad}\nLugar de residencia: \
{self.lugar_residencia}\nSalario: {self.salario}\nAntiguedad: \
{self.antiguedad}")"""
    # Opción 2 ↓
    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "\nAntiguedad:",self.antiguedad,"Años")
    """ Tienen el mismo efecto ambas formas de hacerlo pero con super(), se
    ahorra reemplazar el método padre por uno más adecuado, al llamar a super()
    ejecuta lo arriba y luego viene y corre las instrucciones de abajo """
# Creación de Instancias
Carlos = Persona("Carlos", 22, "Colombia")
print("--- Empleado Carlos ---")
Carlos.descripcion()
print(f"Carlos es instancia de Empleado?: {isinstance(Carlos,Empleado)}")
print(f"Carlos es instancia de Persona?: {isinstance(Carlos,Persona)}")
print()

#################

Anna = Empleado_2(1350,8, "Anna", 27, "Nicaragua")
print("--- Empleada Anna ---")
Anna.descripcion()
print(f"\n¿Anna es instancia de Empleado_2?: {isinstance(Anna,Empleado_2)}")
print(f"¿Anna es instancia de Persona?: {isinstance(Anna,Persona)}")
print()
