import tkinter as tk

from constantes import estilos
from interfaz import items
from interfaz.pantalla import Pantalla


class Combate(Pantalla):
    def __init__(self, contenedor, controlador):
        super().__init__(contenedor, controlador, "Combate")
        self.lista_personajes = None
        self.mensaje = None
        self.texto_resumen = None
        self.carga_widgets()
        self.controlador.actualizar_listas()

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

        self.lista_personajes = items.ListBoxPersonajes(
            frame_personajes_scrolleable,
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

        frame_notas = tk.Frame(
            self,
            background=estilos.Color.FONDO
            )

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
