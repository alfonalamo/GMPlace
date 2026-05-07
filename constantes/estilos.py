import tkinter as tk
from symtable import Class


class Color:
    FONDO = "#00a8e8"
    FONDO_NAV = "#007ea7"
    COMPONENTE = "#003459"
    COMPONENTE_CLARO = "#325C7A"
    TEXTO = "#d8a48f"
    TEXTO_BLANCO = "#ffffff"
    RESALTADO = "#00171f"
    ALIADO="lightgreen"

class Fuente:
    BASICA = ("Arial", 14)
    LIGERA = ("Arial", 12)

ESTILO_PREDETERMINADO  = {
    "font" : Fuente.BASICA,
    "bg" : Color.COMPONENTE,
    "fg" : Color.TEXTO_BLANCO
}

ESTILO_PREDETERMINADO_LIGERO  = {
    "font" : Fuente.LIGERA,
    "background" : Color.COMPONENTE_CLARO,
    "foreground" : Color.TEXTO_BLANCO
}

ESTILO_PREDETERMINADO_BOTON  = {
    "font" : Fuente.BASICA,
    "bg" : Color.COMPONENTE,
    "fg" : Color.TEXTO_BLANCO,
    "relief" : tk.FLAT,
    "activebackground" : Color.FONDO,
    "activeforeground" : Color.TEXTO,
    "disabledforeground" : Color.FONDO,
    "justify" : tk.LEFT
}

