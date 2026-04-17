def mostrar_mensaje(mensaje):
    print(mensaje)

from random import randint

def tirar_dado(n_caras):
    resultado = randint(1,n_caras)
    # print(f"El d{n_caras} ha salido {resultado}")
    return resultado

