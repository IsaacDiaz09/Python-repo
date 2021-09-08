from math import gcd
n1,d1 = [int(i) for i in input().split()]
n2,d2 = [int(j) for j in input().split()]

# Operaciones entre dos fracciones
class Fraccion:
    def __init__(self,num1,num2,den1=1,den2=1):
        self.__num1 = num1
        self.__den1 = den1
        self.__num2 = num2
        self.__den2 = den2

    def muestraFracciones(self):
        return f"{self.__num1}/{self.__den1}\n{self.__num2}/{self.__den2}"
    

    def __simplificar(self,n,d):
        # Se simplifica la fraccion de ser posible
        global simplificado
        simplificado = ""
        for i in range(2,d+1):
            if n % i == 0 and d % i == 0:
                n/=i
                d/=i
        if d == 1:
            # Se devuelve como entero porque como tal la division regresa un flotante
            simplificado = f"{int(n)}/1 -> {int(n)}"
        elif d == 0:
            simplificado = 0
        else:
            simplificado = f"{int(n)}/{int(d)}"
        
    
    def divide(self):
        num = self.__num1*self.__den2
        den = self.__den1*self.__num2
        self.__simplificar(num,den)
        return simplificado


    def multiplica(self):
        num = self.__num1*self.__num2
        den = self.__den1*self.__den2
        self.__simplificar(num,den)
        return simplificado


    def suma(self):
        # if self.__den1 == 0 or self.__den2:
            # return 0
        # Si son homogeneas
        if self.__den1 == self.__den2:
            num = self.__num1+self.__num2
            den = self.__den1
            self.__simplificar(num,den)
            return simplificado
        else:
            # Se halla el minimo comun multiplo de los denominadores con la funcion integrada de math
            mcm_den=int(self.__den1*self.__den2/gcd(self.__den1,self.__den2))
            """ 
            El numerador se cálcula a partir de las veces que se puede dividir el mcm 
            con su denominador correspondiente * el numerador
            """
            num = ((mcm_den/self.__den1)*self.__num1) + ((mcm_den/self.__den2)*self.__num2)
            self.__simplificar(num,mcm_den)
            return simplificado
        

    def resta(self):
        # En escencia la misma lógica con lo del minimo comun multiplo
        # if self.__den1 == 0 or self.__den2:
            # return 0
        if self.__den1 == self.__den2:
            num = self.__num1+self.__num2
            den = self.__den1
            self.__simplificar(num,den)
            return simplificado
        else:
            mcm_den=int(self.__den1*self.__den2/gcd(self.__den1,self.__den2))
            
            num = ((mcm_den/self.__den1)*self.__num1) - ((mcm_den/self.__den2)*self.__num2)
            self.__simplificar(num,mcm_den)
            return simplificado


# Ahora con el modelo base realizado, montarlo en una interfaz gráfica
fracciones = Fraccion(n1,n2,d1,d2)
print()
print(fracciones.muestraFracciones())
print(fracciones.divide())
print(fracciones.multiplica())
print(fracciones.suma())
print(fracciones.resta())
