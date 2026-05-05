import tkinter as tk
from abc import abstractmethod
from tkinter import ttk

from constantes import estilos, config
from interfaz.formulario import FormularioPJ
from interfaz.pantalla import Pantalla
from interfaz.navegador import NavegadorLateral
from logica import util


class Inicio(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Inicio")
        self.carga_widgets()

    def carga_widgets(self):
        tk.Label(
            self,
            text= f"Hola {self.controlador.nombre_master}, aqui empieza",
            justify= tk.LEFT,
            **estilos.ESTILO_PREDETERMINADO
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
            **estilos.ESTILO_PREDETERMINADO
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
                **estilos.ESTILO_PREDETERMINADO
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
            **estilos.ESTILO_PREDETERMINADO,
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
        self.lista_personajes = None
        self.mensaje = None
        self.texto_resumen = None
        self.carga_widgets()
        self.controlador.actualizar_lista_personajes()

    def carga_widgets(self):
        frame_personajes = tk.Frame(
            self,
            background=estilos.Color.FONDO,
            )
        frame_personajes.pack(
            side= tk.LEFT,
            fill= tk.BOTH,
            expand= True,
            padx= 0,
            pady= 0
        )

        frame_personajes_scrolleable = tk.Frame(
            frame_personajes
        )
        frame_personajes_scrolleable.pack(
            side=tk.TOP,
            padx=10,
            pady=10,
            fill=tk.BOTH,
            expand=True
        )
        # barra_scroll_personajes = tk.Scrollbar(
        #     frame_personajes_scrolleable,
        #     background=estilos.Color.FONDO_NAV,
        #     activebackground=estilos.Color.FONDO_NAV
        # )
        # barra_scroll_personajes.pack(
        #     side=tk.RIGHT,
        #     fill=tk.Y,
        #     expand=False
        # )
        self.lista_personajes = tk.Listbox(
            frame_personajes_scrolleable,
            background=estilos.Color.FONDO
            # yscrollcommand=barra_scroll_personajes.set
        )
        self.lista_personajes.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )
        self.controlador.listbox_personajes = self.lista_personajes


        tk.Button(
            frame_personajes,
            text="Añadir enemigo",
            background=estilos.Color.COMPONENTE,
            **estilos.ESTILO_PREDETERMINADO,
            width=20
            ).pack()

        tk.Button(
            frame_personajes,
            text="Actualizar",
            background=estilos.Color.COMPONENTE,
            **estilos.ESTILO_PREDETERMINADO,
            width=20
            # command=self.actualizar_lista_personajes
            ).pack()


        frame_notas = tk.Frame(
            self,
            background=estilos.Color.FONDO
            )



        # barra_scroll_comentario = tk.Scrollbar(
        #     frame_notas,
        #     background=estilos.Color.FONDO_NAV,
        #     activebackground=estilos.Color.FONDO_NAV
        # )

        self.texto_resumen = tk.Text(
            frame_notas
            # yscrollcommand=barra_scroll_comentario.set
        )
        self.texto_resumen.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=0
        )


        # barra_scroll_comentario.pack(
        #     side=tk.RIGHT,
        #     fill=tk.Y,
        #     expand=False
        # )

        self.controlador.cuadro_historial = self.texto_resumen

        self.mensaje = tk.StringVar(frame_notas)

        frame_comentario = tk.Frame(
            frame_notas,
            background=estilos.Color.FONDO
            )
        self.comentario = tk.Entry(frame_comentario,textvariable=self.mensaje)
        self.comentario.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=10,
            pady=0
        )
        self.comentario.bind("<Return>", self.texto_por_intro)
        tk.Button(frame_comentario,text="enviar", command=self.actualizar_texto).pack(
            side= tk.LEFT,
            padx=5

        )

        frame_comentario.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=0,
            pady=10
        )
        frame_notas.pack(
            side= tk.LEFT,
            fill= tk.BOTH,
            expand= True,
            padx= 0,
            pady= 10
        )

    def texto_por_intro(self,event):
        self.actualizar_texto()

    def actualizar_texto(self):
        if not self.mensaje.get().strip() == "" :
            self.controlador.escribir_en_historial(self.mensaje.get())
            self.comentario.delete(0,tk.END)

    # def actualizar_lista_personajes(self):
    #     self.lista_personajes.delete(0,tk.END)
    #     self.controlador.obtener_personajes()
    #     try:
    #         for personaje in self.controlador.personajes.values():
    #             self.lista_personajes.insert(tk.END, personaje.nombre)
    #     except AttributeError:
    #         print("dsandsla", self.controlador.personajes)
    #         pass

class Elementos(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Elementos")
        categorias =  ("Personajes", "Enemigos", "Objetos")
        self.pantalla_activa = "Personajes" # La pantalla que se verá por defecto al inicio
        self.pantallas = {}
        self.contenedor_principal = tk.Frame(self)

        for categoria in categorias:
            pantalla = Subpantalla(self.contenedor_principal, self.controlador, categoria)
            self.pantallas[str(pantalla.nombre)] = pantalla

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
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.carga_widgets()

    def carga_widgets(self):
        nuevo_elemento = tk.Button(
            self,
            text=f"Añadir elemento a {self.nombre}",
            command=self.abre_formulario,
            background=estilos.Color.COMPONENTE,
            foreground=estilos.Color.TEXTO_BLANCO,
            )

        nuevo_elemento.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=5,
            pady=0)

        tk.Text(self).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=10)
        # tk.Label(self, text=self.nombre).pack(side=tk.BOTTOM)

    def abre_formulario(self):
        if self.nombre == "Personajes":
            FormularioPJ(self, self.controlador)
        else:
            toplevel = tk.Toplevel(
                self
            )
            tk.Label(toplevel,text="Formulario no creado aún, sorry").pack()
            tk.Button(toplevel, text="Cerrar", command=lambda: toplevel.destroy()).pack(fill=tk.X)
