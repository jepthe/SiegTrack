import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado

class VentanaLogin(tk.Tk):  # Ventana principal
    def __init__(self):
        super().__init__()
        # Dimensiones de la ventana
        self.ventana_ancho = 1250
        self.ventana_alto = 716
        # Configuración de la ventana (evita que se redimensione)
        self.resizable(False, False)

        # Frame 1: Parte superior, manteniendo tamaño original
        self.frame1 = tk.Frame(self, width=1250, height=358, bg="#d9d9d9")
        self.frame1.pack_propagate(False)  # Evita que el frame cambie de tamaño
        self.frame1.pack(side="top", fill="x")

        # Cargar la imagen desde la carpeta 'images'
        self.cargar_imagen()

        # Frame 2: Parte inferior
        self.frame2 = tk.Frame(self, width=1250, height=358, bg="#a51e1d")
        self.frame2.pack(side="bottom", fill="x")

        # Llama a la función para centrar la ventana una vez que está inicializada
        self.after(1, self.centrar_ventana)

        # Crear elementos en frame2
        self.crear_elementos_frame2()

    def cargar_imagen(self):
        # Carga la imagen usando PIL y ImageTk
        imagen = Image.open("images/SR.png")
        imagen = imagen.resize((360, 350), Image.Resampling.LANCZOS)  # Cambia el tamaño según lo necesites
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un label en frame1 que contenga la imagen y centrarlo
        label_imagen = tk.Label(self.frame1, image=imagen_tk, bg="#d9d9d9")
        label_imagen.image = imagen_tk  # Necesario para evitar que se elimine la imagen
        label_imagen.pack(expand=True)  # Expande el label para que se centre dentro del frame

    def crear_elementos_frame2(self):
        # Crear un contenedor para centrar todos los elementos
        self.contenedor = tk.Frame(self.frame2, bg="#a51e1d")
        self.contenedor.place(relx=0.5, rely=0.5, anchor='center')  # Centra el contenedor en el frame

        # Entry para Usuario con customtkinter
        self.entry_usuario = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="USUARIO",
            width=300,
            height=50,
            fg_color="white",  # Fondo blanco
            corner_radius=20,  # Esquinas redondas
            font=("Open Sans", 15)
        )
        self.entry_usuario.pack(pady=(0, 20))  # Espacio vertical entre los elementos

        # Entry para Contraseña con customtkinter
        self.entry_contrasena = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="CONTRASEÑA",
            show="*",
            width=300,
            height=50,
            fg_color="white",  # Fondo blanco
            corner_radius=20,  # Esquinas redondas
            font=("Open Sans", 15)
        )
        self.entry_contrasena.pack(pady=(0, 20))  # Espacio vertical entre los elementos

        # Checkbox para mostrar contraseña con customtkinter
        self.var_mostrar_contrasena = ctk.BooleanVar()  # Variable para el checkbox
        self.check_mostrar = ctk.CTkCheckBox(self.contenedor, text="Mostrar contraseña", variable=self.var_mostrar_contrasena, command=self.toggle_password)
        self.check_mostrar.pack(pady=(0, 20))  # Espacio vertical entre los elementos

        # Botón Entrar con customtkinter
        self.boton_entrar = ctk.CTkButton(
            self.contenedor,
            text="ENTRAR",
            fg_color="#7d0100",
            text_color="white",
            command=self.entrar,
            height=50,
            corner_radius=20,  # Esquinas redondas
            font=("Open Sans", 20, "bold")  # Texto en negritas
        )
        self.boton_entrar.pack()  # No se necesita margen adicional aquí

    def toggle_password(self):
        # Alternar entre mostrar y ocultar la contraseña
        if self.var_mostrar_contrasena.get():
            self.entry_contrasena.configure(show="")  # Mostrar contraseña
        else:
            self.entry_contrasena.configure(show="*")  # Ocultar contraseña

    def entrar(self):
        # Lógica para el botón "ENTRAR"
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")  # Para propósitos de prueba

    def centrar_ventana(self):
        # Fuerza una actualización de la ventana antes de calcular su geometría
        self.update_idletasks()

        # Obtiene el tamaño de la pantalla
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()

        # Calcula la posición x e y para centrar la ventana
        pos_x = int((pantalla_ancho - self.ventana_ancho) / 2)
        pos_y = int((pantalla_alto - self.ventana_alto) / 2)

        # Establece la geometría de la ventana (dimensiones y posición)
        self.geometry(f"{self.ventana_ancho}x{self.ventana_alto}+{pos_x}+{pos_y}")


