from datetime import datetime
from random import randint

from datos.objetos import Objeto
from datos.personajes import Personaje

def traducir_resultado_bbdd(lista_bruta_personajes):
    lista_objs_pers = list()
    for tupla in lista_bruta_personajes:
        nombre = tupla[1]
        tipo = tupla[3]
        jugador = tupla[4]
        descripcion = tupla[2]
        nivel = tupla[5]
        pv = tupla[6]
        campagna = tupla[13]
        caracteristicas = {"FUE": tupla[7], "CON": tupla[8], "SAB": tupla[9], "INT": tupla[10], "DES": tupla[11],
                           "CAR": tupla[12]}
        personaje = Personaje(nombre, tipo, jugador, descripcion, caracteristicas, pv, campagna, nivel)
        lista_objs_pers.append(personaje)
    return lista_objs_pers

def traducir_objeto_bbdd(lista_bruta):
    lista_objs = list()
    for tupla in lista_bruta:
        campagna = tupla[0]
        nombre = tupla[1]
        personaje = tupla[2]
        descripcion = tupla[3]
        tipo = tupla[4]
        precio = tupla[5]
        modificador = tupla[6]
        objeto = Objeto(campagna, nombre, personaje, descripcion, tipo, precio, modificador)
        lista_objs.append(objeto)
    return lista_objs

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

