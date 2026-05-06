import tkinter as tk
class Color():
    FONDO = "#00a8e8"
    FONDO_NAV = "#007ea7"
    COMPONENTE = "#003459"
    COMPONENTE_CLARO = "#325C7A"
    TEXTO = "#d8a48f"
    TEXTO_BLANCO = "#ffffff"
    RESALTADO = "#00171f"
    ALIADO="lightgreen"

COLOR_FONDO = "grey"
FONT = ("Arial", 14)
# COMPONENT = "red"
ESTILO_PREDETERMINADO  = {
    "font" : FONT,
    "bg" : Color.COMPONENTE,
    "fg" : Color.TEXTO_BLANCO
}

ESTILO_PREDETERMINADO_BOTON  = {
    "font" : FONT,
    "bg" : Color.COMPONENTE_CLARO,
    "fg" : Color.TEXTO_BLANCO,
    "relief" : tk.FLAT,
    "activebackground" : Color.FONDO,
    "activeforeground" : Color.TEXTO,
    "disabledforeground" : COLOR_FONDO,
    "justify" : tk.LEFT
}

