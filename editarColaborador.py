import customtkinter as ctk
from tkinter import messagebox

def miFuncion():
    idEmpleado = str(boxIdEmpleadoSearch.get())
    if idEmpleado == "123":
        messagebox.showinfo(message="Se editó correctamente", title="Alerta")
    else:
        messagebox.showinfo(message="Error, no se encontró el ID del empleado", title="Alerta")

# Función que se ejecuta al presionar el botón de búsqueda
def buscarEmpleado():
    miFuncion()




def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.configure(fg_color="white", text_color="black")

def on_focusout(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(fg_color="white", text_color="#d9d9d9")

def create_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.configure(fg_color="white", text_color="#d9d9d9")
    entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder))
    entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder))

# Función para centrar la ventana en la pantalla
def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = int((ancho_pantalla / 2) - (ancho / 2))
    y = int((alto_pantalla / 2) - (alto / 2))
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


# Configuración inicial de la ventana
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Título de la ventana")

ancho_ventana = 644
alto_ventana = 913
centrar_ventana(ventana, ancho_ventana, alto_ventana)
ventana.resizable(False, False)
ventana.configure(fg_color="#d9d9d9")

label = ctk.CTkLabel(ventana, text="COLABORADOR", fg_color=None, text_color="#a51e1d", font=("Open Sans", 35, "bold"))
label.pack(pady=20)

# Frame principal para contener el Entry de búsqueda
frameBoxSearch = ctk.CTkFrame(ventana, fg_color="#d9d9d9")  
frameBoxSearch.pack(pady=15)

# Crear caja de texto para buscar empleado (centrada)
boxIdEmpleadoSearch = ctk.CTkEntry(frameBoxSearch, font=("Open Sans", 14), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxIdEmpleadoSearch.pack(side="left", padx=(0, 10))  # Solo el Entry está centrado dentro de este Frame
create_placeholder(boxIdEmpleadoSearch, "")

# Frame independiente para el botón de búsqueda, alineado a la derecha
frameLupa = ctk.CTkFrame(ventana, fg_color="#d9d9d9")  # Segundo Frame para el botón, en otro nivel
frameLupa.place(x=540, y=95)  # Ajustar posición del botón a la derecha del Entry

# Botón con un ícono de lupa "🔍" fuera del Entry
boton_busqueda = ctk.CTkButton(frameLupa, 
                               text="🔍", 
                               width=70, 
                               height=35, 
                               corner_radius=40, 
                               text_color="#a51e1d", 
                               fg_color="#d9d9d9",  
                               hover_color="#e0e0e0", 
                               font=("Open Sans", 60, "bold"), 
                               command=miFuncion)
boton_busqueda.pack()

# Crear el resto de las cajas de texto como antes
boxIdEmpleado = ctk.CTkEntry(ventana, font=("Open Sans", 25), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxIdEmpleado.pack(pady=15)
create_placeholder(boxIdEmpleado, "NO. EMPLEADO")

boxNombre = ctk.CTkEntry(ventana, font=("Open Sans", 25), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxNombre.pack(pady=15)
create_placeholder(boxNombre, "NOMBRE")

boxApellidoPaterno = ctk.CTkEntry(ventana, font=("Open Sans", 25), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxApellidoPaterno.pack(pady=15)
create_placeholder(boxApellidoPaterno, "APELLIDO PATERNO")

boxApellidoMaterno = ctk.CTkEntry(ventana, font=("Open Sans", 25), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxApellidoMaterno.pack(pady=15)
create_placeholder(boxApellidoMaterno, "APELLIDO MATERNO")

boxPuesto = ctk.CTkEntry(ventana, font=("Open Sans", 25), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxPuesto.pack(pady=15)
create_placeholder(boxPuesto, "PUESTO")

boxArea = ctk.CTkEntry(ventana, font=("Open Sans", 25), width=450, height=70, corner_radius=40, justify="center", border_width=2, border_color="white")
boxArea.pack(pady=15)
create_placeholder(boxArea, "ÁREA")

# Botón con estilo y cambio de color en hover
boton = ctk.CTkButton(ventana, 
                      text="EDITAR", 
                      width=250, 
                      height=70, 
                      corner_radius=40, 
                      text_color="white", 
                      fg_color="#7d0100",  
                      hover_color="#a51e1d",  
                      font=("Open Sans", 30, "bold"), 
                      command=buscarEmpleado)
boton.pack(pady=20)

ventana.mainloop()







#ambito, que es lo que s[i va a poder hacer]