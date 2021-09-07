# Importe modulos
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk

# Crea ventana
ventana_principal = tk.Tk()

# Conecta con la base de datos
try:
    """
    La variable se debe declarar global porque será usada por 
    las funciones mas adelante
    """
    global conexion
    conexion = sqlite3.connect('db\database.db')
    cursor = conexion.cursor()
except Error:
    messagebox.showerror("Error", Error)

# Frame principal
frame = tk.Frame(ventana_principal, bg="lightgray", bd=20, relief="sunken")
frame.pack(fill='both', expand=True)

# Label frame top
lbl_frame = tk.LabelFrame(frame, text=" ~ Agregar Producto ~ ",
                          relief="ridge", width=90)
lbl_frame.place(x=180, y=8)

lbl_frame_bottom = tk.LabelFrame(
    frame, text="~ Opciones ~", relief="ridge", padx=227)
lbl_frame_bottom.place(x=5, y=467)

# TreeView y barra de deslzaimiento vertical

treeview_db = ttk.Treeview(ventana_principal, columns=(
    "Nombre", "Valor", "Inv"), height=10, padding=4)
treeview_db.column("#0", minwidth=40, width=60, stretch=tk.NO)
treeview_db.column("Nombre", minwidth=200, width=300, stretch=tk.NO)
treeview_db.column("Valor", minwidth=110, width=130, stretch=tk.NO)
treeview_db.column("Inv", minwidth=80, width=100, stretch=tk.NO)

treeview_db.heading("#0", text="Id", anchor=tk.CENTER)
treeview_db.heading("Nombre", text="Nombre del producto", anchor=tk.CENTER)
treeview_db.heading("Valor", text="Valor", anchor=tk.CENTER)
treeview_db.heading("Inv", text="En inventario", anchor=tk.CENTER)
treeview_db.place(x=29, y=240)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=treeview_db.yview)
treeview_db.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=614, y=222, height=230)

# Variables
txt_msg = StringVar()

# Etiquetas
isaac_diaz = tk.Label(
    frame, text="········\nHecho por\nIsaac Díaz\n········", anchor="w", font=("Times", 14), fg="beige", bg="tomato")
isaac_diaz.place(x=10, y=8)

etiqueta_id = tk.Label(
    lbl_frame, text="Id del producto  ", width=19, anchor="w")
etiqueta_id.grid(column=0, row=0, padx=4, pady=4)

etiqueta_nombre_prd = tk.Label(
    lbl_frame, text="Nombre del producto  ", width=19, anchor="w")
etiqueta_nombre_prd.grid(column=0, row=1, padx=4, pady=4)

etiqueta_val_unitario = tk.Label(
    lbl_frame, text="Valor unitario  ", width=19, anchor="w")
etiqueta_val_unitario.grid(column=0, row=2, padx=4, pady=4)

etiqueta_inventario = tk.Label(
    lbl_frame, text="Inventario  ", width=19, anchor="w")
etiqueta_inventario.grid(column=0, row=3, padx=4, pady=4)

# Esta etiqueta es informativa
etiqueta_ms_agrega = tk.Label(frame, textvariable=txt_msg, justify="center",
                              font=("Times 13"), bg="lightgray", width=50, fg="blue")
etiqueta_ms_agrega.place(x=110, y=188)


# Entradas de texto agregar producto
txt_id = tk.Entry(lbl_frame, fg="black", font=("Times 12"),
                  justify=tk.CENTER, width="18")
# Por defecto el cursor se posiciona en esta caja al abrir la ventana
txt_id.focus()
txt_id.grid(column=2, row=0)

txt_nombre = tk.Entry(lbl_frame, fg="black", font=("Times 12"),
                      justify=tk.CENTER, width="18")
txt_nombre.grid(column=2, row=1)

txt_val_unitario = tk.Entry(lbl_frame, fg="black", font=("Times 12"),
                            justify=tk.CENTER, width="18")
txt_val_unitario.grid(column=2, row=2)

txt_inventario = tk.Entry(lbl_frame, fg="black", font=("Times 12"),
                          justify=tk.CENTER, width="18")
txt_inventario.grid(column=2, row=3)

# Funciones - Aquí se controla basicamente todo -


def centrar(ancho, alto):
    # --- Centrar ventana  en la pantalla respecto al tamaño de la misma ---
    screen_width = ventana_principal.winfo_screenwidth()
    screen_height = ventana_principal.winfo_screenheight()
    centrarX = (screen_width - ancho)//2
    centrarY = (screen_height - alto)//2
    return "{}x{}+{}+{}".format(ancho, alto, centrarX, centrarY)


""" 
Obtiene las filas de la tabla y las posiciona en el elemento TreeView
"""

def return_rows():
    global Id
    Id = []
    global nombre
    nombre = []
    val = []
    inv = []

    cursor.execute('SELECT * FROM registro_productos')
    filas = cursor.fetchall()
    for fila in filas:
        Id.append(str(fila[0]))
        nombre.append(str(fila[1]))
        val.append(str(fila[2]))
        inv.append(str(fila[3]))

    for i in range(len(filas)):
        treeview_db.insert("", tk.END, text=Id[i],
                           values=(nombre[i], val[i], inv[i]))


""" 
indice_db() obtiene el indice del producto en la base de datos cuando se
hace click en la fila, se activa por evento (Seleccionar una fila) 
"""


def obtiene_id():
    cursor.execute("SELECT * FROM registro_productos")
    filas = cursor.fetchall()
    global id
    # Si se ha seleccionado alguna fila, traiga lo que hay en el campo 'text' que equivale al ID
    if (filas := treeview_db.selection()):
        id = treeview_db.item(filas)['text']

# El evento de seleccionar una fila llama a la


def indice_db(event):
    obtiene_id()


"""
Genera una segunda ventana, hija de la principal para 
mostrar el menu de actualizar producto
"""

def abrir_editar():

    # Dentro de ella se define guarda() la cual recoge lo que haya en las cajas
    # de texto, los pone en una tupla y actualiza el registro en la Base de Datos
    def guarda():
        valores_edit = [edit_nombre.get(), edit_val.get(),
                        edit_inv.get()] + [str(id)]
        # Este condicional impide que se ejecute el registro si se dejo algun
        # campo en blanco y muestra una advertencia
        if "" in valores_edit:
            messagebox.showerror(
                "Error", "No puede dejar ningún campo en blanco.")
            datos_validos = False
        else:
            datos_validos = True

        # Si se paso el condicional con exito se ordena actualizar con los datos ingresados
        if datos_validos:
            try:
                query_add = "UPDATE registro_productos SET Nombre = ?,Valor = ?,Inventario = ? WHERE Id = ?"
                cursor.execute(query_add, valores_edit)
                # Guarda los cambios
                conexion.commit()
                # Para que se vea el cambio reflejado en la TreeView hay que limpiarlo
                # y volver a posicionar las filas halladas (Actualizar)
                treeview_db.delete(*treeview_db.get_children())
                return_rows()
                # Cierra la ventana hija
                vnt_edit.destroy()
                # Mensaje informativo
                txt_msg.set("El registro se actualizó con exito")

            except Error:
                txt_msg.set("No se pudo actualizar el registro")
        else:
            """
            Si dejo algun campo en blanco, se cierra la ventana 
            y el usuario debe intentarlo de nuevo.
            """
            vnt_edit.destroy()
            
    # Se crea la ventana hija y se le dan sus propiedades

    vnt_edit = tk.Toplevel(ventana_principal)
    vnt_edit.geometry(centrar(320,230))
    vnt_edit.title("Editar registro")
    vnt_edit.resizable(False, False)
    vnt_edit.iconphoto(False, tk.PhotoImage(file='icono_vnt_edit.png'))

    # Con estas instrucciones se crean los elementos de la ventana hija (etiquetas, cajas, botones)
    # Ademas se obtienen los datos de la fila seleccionada y se posicionan en unos campos desactivados

    try:
        cursor.execute(
            "SELECT Nombre,Valor,Inventario FROM registro_productos WHERE Id = ?", (id,))
        datos = cursor.fetchone()
        nombre = StringVar()
        nombre.set(datos[0])
        valor = StringVar()
        valor.set(datos[1])
        inv = StringVar()
        inv.set(datos[2])
        conexion.commit()
        espacio = tk.Label(vnt_edit, pady=4, padx=4)
        espacio.grid(column=0, row=0)
        lbl_nombre = tk.Label(vnt_edit, text="  Nombre actual\t")
        lbl_valor = tk.Label(vnt_edit, text="  Valor actual\t")
        lbl_inv = tk.Label(vnt_edit, text="  Inventario actual\t")
        lbl_n_nombre = tk.Label(vnt_edit, text="  Nuevo nombre\t")
        lbl_n_val = tk.Label(vnt_edit, text="  Nuevo valor\t")
        lbl_n_inv = tk.Label(vnt_edit, text="Nuevo inventario\t")
        nombre = tk.Entry(vnt_edit, justify=tk.CENTER, width="18",
                          state=tk.DISABLED, font=("Times 12"), textvariable=nombre)
        valor = tk.Entry(vnt_edit, justify=tk.CENTER, width="18",
                         state=tk.DISABLED, font=("Times 12"), textvariable=valor)
        inv = tk.Entry(vnt_edit, justify=tk.CENTER, width="18",
                       state=tk.DISABLED, font=("Times 12"), textvariable=inv)
        edit_nombre = tk.Entry(vnt_edit, justify=tk.CENTER,
                               width="18", font=("Times 12"))
        edit_val = tk.Entry(vnt_edit, justify=tk.CENTER,
                            width="18", font=("Times 12"))
        edit_inv = tk.Entry(vnt_edit, justify=tk.CENTER,
                            width="18", font=("Times 12"))
        lbl_nombre.grid(column=1, row=1, sticky= "w")
        lbl_valor.grid(column=1, row=2, sticky= "w")
        lbl_inv.grid(column=1, row=3, sticky= "w")
        lbl_n_nombre.grid(column=1, row=4, sticky= "w")
        lbl_n_val.grid(column=1, row=5, sticky= "w")
        lbl_n_inv.grid(column=1, row=6, sticky= "w")
        nombre.grid(column=2, row=1)
        valor.grid(column=2, row=2)
        inv.grid(column=2, row=3)
        edit_nombre.grid(column=2, row=4)
        edit_val.grid(column=2, row=5)
        edit_inv.grid(column=2, row=6)

        boton_guardar = tk.Button(
            vnt_edit, text="Guardar", padx=12, font=("Times 12"), command=guarda)

        def evento_guarda(event):
            guarda()
            boton_editar["state"] = tk.NORMAL

        boton_guardar.bind_all("<Return>", evento_guarda)
        boton_cancelar = tk.Button(vnt_edit, text="Cancelar", padx=12, font=(
            "Times 12"), command=vnt_edit.destroy)
        boton_guardar.place(x=60, y=175)
        boton_cancelar.place(x=180, y=175)
        txt_msg.set("")

    # Si no se ha seleccionado nada y se presiona el boton, salta un aviso mostrando el problema
    except:
        # Cuando se clickea en aceptar se cierra la ventana y se restaura el boton
        def cerrar():
            vnt_edit.destroy()
            boton_editar["state"] = tk.NORMAL

        txt_msg.set("No se ha seleccionado ningún producto")
        global msg_error, btton_error
        msg_error = tk.Label(vnt_edit, text="No seleccionó ningún\nproducto a editar", font=(
            "Times 14"), justify=tk.CENTER, width="24", fg="red")
        msg_error.grid(column=0, row=0)
        btton_error = tk.Button(vnt_edit, text="Aceptar", padx=12, font=(
            "Times 12"), command=cerrar)
        btton_error.grid(column=0, row=1)
        vnt_edit.geometry(centrar(250, 100))


# Esta funcion recoge los datos de las cajas de texto, lo ordena y lo añade a la
# tabla de la Base de Datos en cuestion

def agrega_reg():
    def __limpiarCampos():
        txt_id.focus()
        txt_id.delete(0,"end")
        txt_nombre.delete(0,"end")
        txt_val_unitario.delete(0,"end")
        txt_inventario.delete(0,"end")

    def __validaCamposVacios():
        for i in [txt_id.get().strip(), txt_nombre.get().strip(), txt_val_unitario.get().strip(), txt_inventario.get().strip()]:
            if i == "":
                return False
            return True

    try:
        if txt_id.get().strip() in Id:
            messagebox.showwarning("Añadir producto", f"El Id {txt_id.get()} ya se encuentra en uso")
            txt_id.delete(0,"end")
            txt_id.focus()

        elif  __validaCamposVacios() is False:
            messagebox.showwarning("Añadir registro", "No es posible dejar ningún campo en blanco.")
            __limpiarCampos()

        elif txt_nombre.get().strip() in nombre:
            messagebox.showerror("Producto repetido",f"El producto '{txt_nombre.get().strip()}' ya se encuentra registrado.")
            __limpiarCampos()

        else:
            values_to_add = tuple([
            int(txt_id.get().strip()), 
            txt_nombre.get().strip(), 
            float(txt_val_unitario.get().strip()), 
            int(txt_inventario.get().strip())
            ])

            # Si los datos pasaron pasan a ser añadidos

            cursor.execute("INSERT INTO registro_productos (Id,Nombre,Valor,Inventario) VALUES (?,?,?,?)", values_to_add)
            conexion.commit()
            # Se actualiza el ListBox para poder ver los cambios
            treeview_db.delete(*treeview_db.get_children())
            return_rows()
            # Mensaje informativo
            txt_msg.set(f"Se ha registrado '{values_to_add[1]}' exitosamente")
            __limpiarCampos()

    except ValueError:
        messagebox.showerror("Error", "Ingresó datos inválidos, no se puede añadir el producto.")
        __limpiarCampos()


"""
elimina_reg() Elimina el registro seleccionado (ya que ha obtenido su Id) 
de la Base de Datos
"""

def elimina_reg():
    try:
        query = "SELECT Nombre,Valor,Inventario FROM registro_productos WHERE Id = ?"
        cursor.execute(query, (id,))
        datos = cursor.fetchone()
        nombre = (datos[0])
        conexion.commit()
        # Instruccion Sql
        cursor.execute("DELETE FROM registro_productos WHERE Id = ?", (id,))
        txt_msg.set(f"Se eliminó '{nombre}' de su Base de Datos")

        # Guarda cambios y actualiza
        conexion.commit()
        treeview_db.delete(*treeview_db.get_children())
        return_rows()
    except:
        txt_msg.set("Asegurese de haber seleccionado alguna fila")


# Botones: Frame principal y frame inferior
boton_agrega = tk.Button(ventana_principal, text="Agregar",
                         padx=12, font=("Times 13"), command=agrega_reg)
boton_agrega.place(x=310, y=170)

boton_editar = tk.Button(lbl_frame_bottom, text="Editar",
                         padx=12, font=("Times 13"), command=abrir_editar)
boton_editar.grid(column=0, row=0)

boton_eliminar = tk.Button(lbl_frame_bottom, text="Eliminar",
                           padx=12, font=("Times 13"), command=elimina_reg)
boton_eliminar.grid(column=1, row=0)

# Enlace a eventos


def evento_agrega(event):
    # Se deshabilita el boton cuando este esta activo
    boton_agrega["state"] = tk.DISABLED
    agrega_reg()
    boton_agrega["state"] = tk.NORMAL


treeview_db.bind("<<TreeviewSelect>>", indice_db)     # Evento seleccionar fila TreeView
boton_agrega.bind_all("<Return>", evento_agrega)      # Evento tecla: 'Enter'

# Ejecucion aplicacion
if __name__ == "__main__":
    return_rows()
    ventana_principal.title("Base de datos Supermercado")
    ventana_principal.resizable(False, False)
    ventana_principal.configure(bg="gray", bd=15, relief="ridge")
    ventana_principal.geometry(centrar(700, 590))
    ventana_principal.iconphoto(False, tk.PhotoImage(file='icono.png'))
    ventana_principal.mainloop()
