import sqlite3 as sql

def conectar_bbdd(): # Este metodo esta para poder cambiar la bbdd facil si hace falta
    return sql.connect("datos/bbdd.db")

def crear_tabla_personajes():
    conn = conectar_bbdd()
    try:
        conn.execute(
            """CREATE TABLE personajes (
                id text primary key,
                nombre text,
                descripcion text,
                tipo text,
                jugador text,
                nivel integer,
                pv integer,
                fue integer ,
                con integer ,
                sab integer ,
                int integer ,
                des integer ,
                car integer ,
                campagna text
            )"""
        )
        conn.commit()
    except sql.OperationalError:
        print("Existe tabla de personajes")
    conn.close()

def insertar_personaje(personaje):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = (f"INSERT INTO personajes VALUES('{personaje.id}','{personaje.nombre}', '{personaje.descripcion}', "
                   f"'{personaje.tipo}', '{personaje.jugador}', {personaje.nivel}, {personaje.pv_actual}, "
                   f"{personaje.caracteristicas["FUE"]}, {personaje.caracteristicas["CON"]}, "
                   f"{personaje.caracteristicas["SAB"]}, {personaje.caracteristicas["INT"]}, "
                   f"{personaje.caracteristicas["DES"]}, {personaje.caracteristicas["CAR"]}," 
                   f"'{personaje.campagna}')")
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def modificar_personaje(id_antiguo):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = (f"UPDATE personajes WHERE id={id_antiguo}")
    instruccion = (f"INSERT INTO personajes VALUES('{personaje.id}','{personaje.nombre}', '{personaje.descripcion}', "
                   f"'{personaje.tipo}', '{personaje.jugador}', {personaje.nivel}, {personaje.pv_actual}, "
                   f"{personaje.caracteristicas["FUE"]}, {personaje.caracteristicas["CON"]}, "
                   f"{personaje.caracteristicas["SAB"]}, {personaje.caracteristicas["INT"]}, "
                   f"{personaje.caracteristicas["DES"]}, {personaje.caracteristicas["CAR"]}," 
                   f"'{personaje.campagna}')")
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def borrar_personaje(id_antiguo):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = (f"DELETE FROM personajes WHERE id='{id_antiguo}'")
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def leer_personajes(campagna):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    print("leer_personajes: ", campagna)
    instruccion = f"SELECT * FROM personajes WHERE campagna = '{campagna}'"
    print("instruccion ",instruccion)
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    print("resultado", resultado)
    conn.commit()
    conn.close()
    return resultado

def leer_aliados(campagna):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    print("leer_personajes: ", campagna)
    instruccion = f"SELECT * FROM personajes WHERE campagna = '{campagna}' AND tipo = 'pj'"
    print("instruccion ",instruccion)
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    print("resultado", resultado)
    conn.commit()
    conn.close()
    return resultado

def leer_enemigos(campagna):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    print("leer_personajes: ", campagna)
    instruccion = f"SELECT * FROM personajes WHERE campagna = '{campagna}' AND tipo = 'enemigo'"
    print("instruccion ",instruccion)
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    print("resultado", resultado)
    conn.commit()
    conn.close()
    return resultado

def crear_tabla_campa():
    conn = conectar_bbdd()
    try:
        conn.execute(
            """CREATE TABLE campas (
                nombre text primary key,
                master text,
                historial text
            )"""
        )
        conn.commit()
    except sql.OperationalError:
        print("Existe tabla de campagnas")
    conn.close()

def leer_campas():
    conn = conectar_bbdd()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM campas "
    )
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado

def insertar_campa(datos):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"INSERT INTO campas VALUES('{datos['campagna']}','{datos['nombre']}', '{datos['historial']}')"
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

