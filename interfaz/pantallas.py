import tkinter as tk
from abc import abstractmethod
from tkinter import ttk

from constantes import estilos, config
from interfaz.formulario import FormularioPJ
from interfaz.pantalla import Pantalla
from interfaz.navegador import NavegadorLateral

class Inicio(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Inicio")
        self.carga_widgets()

    def carga_widgets(self):
        tk.Label(
            self,
            text= "Hola aventurero, aqui empieza",
            justify= tk.LEFT,
            **estilos.ESTILO_DEFAULT
            ).pack(
            side= tk.TOP,
            fill= tk.BOTH,
            expand= True,
            padx= 22,
            pady= 11
        )
        opciones = tk.Frame(self)
        opciones.configure(background=estilos.Color.FONDO)
        opciones.pack(
            side= tk.TOP,
            fill= tk.BOTH,
            expand= True,
            padx= 22,
            pady=5
        )
        tk.Label(
            opciones,
            text= "Blablabla",
            justify= tk.CENTER,
            **estilos.ESTILO_DEFAULT
        ).pack(
            side= tk.TOP,
            fill= tk.BOTH,
            expand= True
        )

        # ToDo: BORRAR!
        diccionario = {
            "A" : "a",
            "B" : "b",
            "C" : "c"
        }

        for (key, value) in config.MODOS.items():
            tk.Radiobutton(
                opciones,
                text= key,
                variable= self.opcion_seleccionada,
                value= value,
                selectcolor= estilos.Color.TEXTO_BLANCO,
                highlightcolor="red",
                activebackground= estilos.Color.FONDO,
                activeforeground= estilos.Color.TEXTO_BLANCO,
                **estilos.ESTILO_DEFAULT
            ).pack(
                side= tk.LEFT,
                fill= tk.BOTH,
                expand= True,
                padx= 5,
                pady= 5
            )

        tk.Button(
            self,
            text= "CAMPAÑA",
            # command= self.ir_campagna,
            command= lambda: self.controlador.muestra_pantalla("Campaña"),
            **estilos.ESTILO_DEFAULT,
            relief= tk.FLAT,
            # activebackground=estilos.Color.FONDO,
            activebackground=estilos.Color.FONDO,
            activeforeground=estilos.Color.TEXTO,
        ).pack(
            side= tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=5
        )

class Combate(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Combate")
        self.carga_widgets()

    def carga_widgets(self):
        frame_personajes = tk.Frame(self)
        tk.Label(
            frame_personajes,
            text="placeholder",
            width=20
            ).pack()
        frame_personajes.pack(
            side= tk.LEFT,
            fill= tk.BOTH,
            expand= True,
            padx= 0,
            pady= 0
        )
        frame_notas = tk.Frame(self)

        self.texto_resumen = tk.Text(frame_notas)
        self.texto_resumen.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=0
        )

        self.mensaje = tk.StringVar(frame_notas)

        frame_comentario = tk.Frame(frame_notas)
        comentario = tk.Entry(frame_comentario,textvariable=self.mensaje)
        comentario.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=0,
            pady=0
        )
        tk.Button(frame_comentario,text="enviar", command=self.actualizar_texto).pack(side= tk.BOTTOM)

        frame_comentario.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=10,
            pady=0
        )
        frame_notas.pack(
            side= tk.LEFT,
            fill= tk.BOTH,
            expand= True,
            padx= 0,
            pady= 10
        )

    def actualizar_texto(self):
        self.texto_resumen.insert(tk.END,self.mensaje.get())
        self.texto_resumen.insert(tk.END,"\n")

class Elementos(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Elementos")
        categorias =  ("Objetos", "Personajes", "Enemigos")
        self.pantallas = {}
        self.contenedor_principal = tk.Frame(self, background="green")

        for categoria in categorias:
            pantalla = Subpantalla(self.contenedor_principal, self.controlador, categoria)
            self.pantallas[str(pantalla.nombre)] = pantalla

        print("pantallas ", self.pantallas)
        self.pantalla_activa = "Personajes" # La pantalla que se verá por defecto al inicio
        controlador.muestra_pantalla(self, self.pantalla_activa)

        self.barra_navegacion = NavegadorLateral(self, self.controlador, self.pantallas.values())
        self.carga_widgets()


    def carga_widgets(self):
        self.barra_navegacion.pack(
            side= tk.LEFT,
            fill= tk.Y,
            expand= False,
            padx= 0,
            pady= 0
        )
        self.contenedor_principal.pack(
            side = tk.LEFT,
            fill = tk.BOTH,
            expand= True,
            padx= 0,
            pady= 0
        )
        self.contenedor_principal.configure(background=estilos.Color.FONDO)
        self.contenedor_principal.grid_columnconfigure(0, weight=1)
        self.contenedor_principal.grid_rowconfigure(0, weight=1)

class Subpantalla(Pantalla):
    def __init__(self, contenedor, controlador, nombre):
        super().__init__(contenedor, controlador, nombre)
        self.carga_widgets()

    def carga_widgets(self):
        print("self",self)
        nuevo_elemento = tk.Button(
            self,
            text=f"Añadir elemento a {self.nombre}",
            command=lambda: FormularioPJ(self,self.controlador),
            background="blue"
            )

        nuevo_elemento.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=5,
            pady=0)

        tk.Text(self).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=20)
        # tk.Label(self, text=self.nombre).pack(side=tk.BOTTOM)
