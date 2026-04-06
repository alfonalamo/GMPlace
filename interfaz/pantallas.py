import tkinter as tk
from abc import abstractmethod

from constantes import estilos, config

class Pantalla(tk.Frame):
    def __init__(self, contenedor, controlador, nombre):
        super().__init__(contenedor)
        self.configure(background=estilos.Color.FONDO)
        self.controlador = controlador
        self.opcion_seleccionada = tk.StringVar(self, value="a")
        self.nombre = nombre

    @abstractmethod
    def carga_widgets(self):
        pass

class Inicio(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Inicio")
        self.carga_widgets()
    def carga_widgets(self):
        tk.Label(
            self,
            text= "Hola aventurero, aqui empieza",
            justify= tk.CENTER,
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
            command= lambda: self.controlador.muestra_frame("Campaña"),
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

class Campana(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Campaña")
        self.carga_widgets()

    def carga_widgets(self):
        tk.Label(
            self,
            # text= "Hola aventurero",
            textvariable= self.nombre,
            justify= tk.CENTER,
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

        # self.nombre_master.pack()
        tk.Button(
            self,
            text= "Nombre",
            # command= self.update_nombre,
            **estilos.ESTILO_DEFAULT,
            relief= tk.GROOVE,
            activebackground=estilos.Color.FONDO,
            activeforeground=estilos.Color.TEXTO_BLANCO,
        ).pack(
            side= tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=5
        )

        tk.Button(
            self,
            text= "Inicio",
            # command= self.ir_campagna,
            command= lambda: self.controlador.muestra_frame(Inicio),
            **estilos.ESTILO_DEFAULT,
            relief= tk.GROOVE,
            activebackground=estilos.Color.FONDO,
            activeforeground=estilos.Color.TEXTO_BLANCO,
        ).pack(
            side= tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=5
        )

    #
    # def update_nombre(self):
    #     print(self.nombre.set(f"Hola {self.nombre_master.get()}"))

class Personajes(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Personajes")
        self.carga_widgets()
    def carga_widgets(self):
        tk.Label(
            self,
            text= "Hola aventurero",
            justify= tk.CENTER,
            **estilos.ESTILO_DEFAULT
            ).pack(
            side= tk.TOP,
            fill= tk.BOTH,
            expand= True,
            padx= 22,
            pady= 11
        )