from datetime import datetime
from random import randint


def mostrar_mensaje(mensaje):
    print(mensaje)

def crear_mensaje(msj):
    tiempo = datetime.now()
    tiempoformateado = tiempo.strftime("%d/%m/%y %H:%M")
    return f"{tiempoformateado} {msj}\n"



def tirar_dado(n_caras):
    resultado = randint(1,n_caras)
    # print(f"El d{n_caras} ha salido {resultado}")
    return resultado

def obtener_caracteristicas(dic):
    dic_traducido = {}
    for key,value in dic.items:
        dic_traducido[key] = value.get()
    print(dic_traducido)

def calcular_modificador(valor):
    modificador = (int(valor) - 10)
    return int(modificador)

def tratar_nombre(nombre_bruto):
    nombre_bruto = str(nombre_bruto).title()
    nombre_tratado = nombre_bruto.replace(" ", "_")
    return nombre_tratado

def calcular_ca(valor_constitucion):
    return int(valor_constitucion * 3)

def calcular_pv(valor_constitucion):
    return int(valor_constitucion * 6)

