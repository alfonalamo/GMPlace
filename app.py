import tkinter as tk
from tkinter import simpledialog, filedialog
import os
app = tk.Tk()

nombre = tk.StringVar(app)
entrada = tk.StringVar(app)

app.geometry("300x600")
app.configure(background="black")
tk.Wm.wm_title(app,"Gm place")

tk.Button(
    app,
    text="click",
    font=("Arial", 12),
    bg="#00a8e8",
    fg="white",
    command=lambda: print(f"Hola {entrada.get()}")
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Label(
    app,
    text="Etiqueta",
    textvariable=nombre,
    font=("Arial", 12),
    bg="#00a8e8",
    fg="white",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True
)

tk.Entry(
    app,
    text="Etiqueta",
    font=("Arial", 12),
    bg="#00a8e8",
    fg="white",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True
)



app.mainloop()