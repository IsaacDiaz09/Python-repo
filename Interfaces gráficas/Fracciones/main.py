# Importes necesarios
from math import gcd
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk

# Operaciones entre dos fracciones

class Ventana:
    def __init__(self, r=None):
        self.root = r
        self.root.geometry("400x290")
        self.root.title("Operaciones con Fracciones")
        self.root.configure(bg="white", bd=15, relief="ridge")
        self.root.resizable(False, False)
        self.root.iconphoto(False, tk.PhotoImage(file='ico.png'))

        # Las lineas de fraccion
        self.raya = tk.Label(self.root, text="────", bg="white", height=1)
        self.raya.place(x=18, y=40)

        self.raya2 = tk.Label(self.root, text="────", bg="white", height=1)
        self.raya2.place(x=118, y=40)

        self.raya3 = tk.Label(self.root, text="────", bg="white", height=1)
        self.raya3.place(x=148, y=180)

        self.isaac_diaz = tk.Label(
        self.root, text="········\nHecho por\nIsaac Díaz\n········", anchor="w",font=("Times",14),fg="beige",bg="mediumorchid")
        self.isaac_diaz.place(x=275,y=165)
        # Label del ComboBox
        self.Lblcombo = tk.Label(
            self.root, bg="white", text="Seleccione la operación", font=("Times 13"))
        self.Lblcombo.place(x=185, y=20)
        # Label msg de error
        global msg_error
        # Se debe hacer variable global porque solo esta definida dentro del inicializador
        msg_error = StringVar()
        self.error = tk.Label(self.root, bg="white", fg="red",
                              textvariable=msg_error, font=("Times 13"))
        self.error.place(x=20, y=230)

        # Label de signo
        self.signovar = StringVar()
        self.signovar.set("y")
        self.signo = tk.Label(
            self.root, textvariable=self.signovar, bg="white", font=("Times 13"))
        self.signo.place(x=85, y=40)
        # Label auxiliar respuesta
        self.equivale = StringVar()
        self.auxRes = tk.Label(
            self.root, textvariable=self.equivale, bg="white", font=("Times 13"))
        self.auxRes.place(x=215, y=180)
        # Numerador y denomiador de las Fracciones
        self.num1 = tk.Entry(self.root, font=("Times 14"), bg="azure",
                             justify=tk.CENTER, width="5", validate="key",
                             validatecommand=(self.root.register(self.__validaEntry), "%S"))
        self.num1.place(x=20, y=20)

        self.den1 = tk.Entry(self.root, font=("Times 14"), bg="azure",
                             justify=tk.CENTER, width="5", validate="key",
                             validatecommand=(self.root.register(self.__validaEntry), "%S"))
        self.den1.place(x=20, y=60)

        self.num2 = tk.Entry(self.root, font=("Times 14"), bg="azure",
                             justify=tk.CENTER, width="5", validate="key",
                             validatecommand=(self.root.register(self.__validaEntry), "%S"))
        self.num2.place(x=120, y=20)

        self.den2 = tk.Entry(self.root, fg="black", font=("Times 14"), bg="azure",
                             justify=tk.CENTER, width="5", validate="key",
                             validatecommand=(self.root.register(self.__validaEntry), "%S"))
        self.den2.place(x=120, y=60)

        # Fraccion resultado
        self.numRes = StringVar()
        self.denRes = StringVar()
        self.numResultado = tk.Entry(self.root, textvariable=self.numRes, font=("Times 14"), bg="azure",
                                     justify=tk.CENTER, width="5")
        self.numResultado.place(x=150, y=160)

        self.denResultado = tk.Entry(self.root, textvariable=self.denRes, font=("Times 14"), bg="azure",
                                     justify=tk.CENTER, width="5")
        self.denResultado.place(x=150, y=200)

        # Boton calcular
        self.calcula = tk.Button(self.root, fg="black", font=(
            "Times 14"), text="Calcular", command=self.calcular)
        # Lista desplegable ComboBox
        self.calcula.place(x=140, y=105)
        self.combo = ttk.Combobox(self.root, state="readonly", values=[
                                  "Sumar", "Restar", "Dividir", "Multiplicar"])
        self.combo.place(x=196, y=55)
        # Cuando se selecciona un elemento este se puede obtener
        self.combo.bind_all("<<ComboboxSelected>>",
                            self.__evento_seleccion_comboBx)

    def __evento_seleccion_comboBx(self, event):
        global seleccion
        seleccion = self.combo.get()
        if seleccion == "Sumar":
            self.signovar.set("+")
        if seleccion == "Restar":
            self.signovar.set("-")
        if seleccion == "Multiplicar":
            self.signovar.set("*")
        if seleccion == "Dividir":
            self.signovar.set("÷")

    def calcular(self):
        # Se obtienen los valores necesarios para las operaciones
        """ 
        Manejo de errores en caso de que no se seleccione 
        alguna operacion o se deje un campo en blanco
        """

        try:
            global n1, d1, n2, d2
            n1 = int(self.num1.get())
            d1 = int(self.den1.get())
            n2 = int(self.num2.get())
            d2 = int(self.den2.get())

        
            if seleccion == "Sumar":
                self.suma(n1, d1, n2, d2)
            elif seleccion == "Restar":
                self.resta(n1, d1, n2, d2)
            elif seleccion == "Multiplicar":
                self.multiplica(n1, d1, n2, d2)
            elif seleccion == "Dividir":
                self.divide(n1, d1, n2, d2)
        
        except NameError:
            msg_error.set("Debe seleccionar alguna operación")
        except ValueError:
            msg_error.set("No puede dejar ningún campo vacio")

    # Permite que solo se escriban numeros en las entradas de texto

    def __validaEntry(self, text):
        return text.isdigit()

    def __simplificar(self, n, d):
        # Se limpia el campo para que no se muestre el valor anterior en la operación actual
        self.equivale.set("")

        # Se simplifica la fraccion de ser posible
        for i in range(2, d+1):
            if n % i == 0 and d % i == 0:
                n /= i
                d /= i
        """ 
        Se entrega la respuesta en los Entry correspondientes y se pasa a entero para
        que no salga con coma flotante, ej: 1.0 -> 1
        """

        if d == 1:
            self.numRes.set(int(n))
            self.denRes.set(1)
            self.equivale.set(f"=> {int(n)}")

        elif d == 0:
            self.numRes.set(int(n))
            self.denRes.set(0)
            self.equivale.set("=> 0")
        else:
            self.numRes.set(int(n))
            self.denRes.set(int(d))

    def divide(self, num1, den1, num2, den2):
        num = num1*den2
        den = den1*num2
        self.__simplificar(num, den)

    def multiplica(self, num1, den1, num2, den2):
        num = num1*num2
        den = den1*den2
        self.__simplificar(num, den)

    def suma(self, num1, den1, num2, den2):
        msg_error.set("")

        # Si son homogeneas
        if den1 == den2:
            num = num1+num2
            den = den1
            self.__simplificar(num, den)

        else:
            # Se halla el minimo comun multiplo de los denominadores con la funcion integrada de math
            try:
                mcm_den = int(den1*den2 / gcd(den1, den2))
                """ 
                El numerador se cálcula a partir de las veces que se puede dividir el mcm 
                con su denominador correspondiente * el numerador
                """
                num = ((mcm_den/den1)*num1) + ((mcm_den/den2)*num2)
                self.__simplificar(num, mcm_den)
            except ZeroDivisionError:
                """
                Como no es posible dividir entre 0 (si el denomiador toma ese valor). Es incorrecto 
                decir que se omite la fraccion que tiene den=0 y se muestra la que no, 
                se muestra un error entonces con tal de que el programa no caiga.
                """
                self.numRes.set("~")
                self.denRes.set("~")
                msg_error.set("Dividir por 0 no está definido")
                
    def resta(self, num1, den1, num2, den2):
        msg_error.set("")
        # En escencia la misma lógica del minimo comun multiplo
        if den1 == den2:
            num = num1+num2
            den = den1
            self.__simplificar(num, den)

        else:
            try:
                mcm_den = int(den1*den2 / gcd(den1, den2))
                num = ((mcm_den/den1)*num1) - ((mcm_den/den2)*num2)
                self.__simplificar(num, mcm_den)
            except ZeroDivisionError:
                # Aqui el mismo manejo que en suma
                self.numRes.set("~")
                self.denRes.set("~")
                msg_error.set("Dividir por 0 no está definido")

if __name__ == '__main__':
    r = tk.Tk()
    mi_ventana = Ventana(r)
    r.mainloop()
