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

def recuperar_personajes(campagna):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM personajes WHERE campagna = '{campagna}'"
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado

def recuperar_aliados(campagna):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM personajes WHERE campagna = '{campagna}' AND tipo = 'pj'"
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado

def recuperar_enemigos(campagna):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM personajes WHERE campagna = '{campagna}' AND tipo = 'enemigo'"
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
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

def crear_tabla_objetos():
    conn = conectar_bbdd()
    try:
        conn.execute(
            """CREATE TABLE objetos (
                campagna text,
                nombre text,
                personaje text,
                descripcion text,
                tipo text,
                precio double,
                modificador integer
            )"""
        )
        conn.commit()
    except sql.OperationalError:
        print("Existe tabla de objetos")
    conn.close()

def insertar_objeto(objeto):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = (f"INSERT INTO objetos VALUES('{objeto.campagna}','{objeto.nombre}','{objeto.personaje}',"
                   f"'{objeto.descripcion}', '{objeto.tipo}', {objeto.precio}, {objeto.modificador})")
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def recuperar_objetos(campagna, id_pj = "comun"):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM objetos WHERE campagna = '{campagna}' AND personaje='{id_pj}' "
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado

def recuperar_armas(personaje):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = (f"SELECT nombre FROM objetos WHERE campagna = '{personaje.campagna}' AND tipo = 'arma' "
                   f"AND personaje = '{personaje.id}' ")
    cursor.execute(
        instruccion
    )
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado

def modifcar_objeto(objeto, nombre_ant):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = (f"UPDATE objetos SET nombre = '{objeto.nombre}',"
                   f"descripcion = '{objeto.descripcion}',"
                   f"tipo = '{objeto.tipo}',"
                   f"precio = {objeto.precio}, "
                   f"modificador = {objeto.modificador} "
                   f"WHERE nombre = '{nombre_ant}'")
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def borrar_objeto(objeto):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"DELETE FROM objetos WHERE nombre='{objeto.nombre}'"
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def borrar_objeto_pj(objeto):
    conn = conectar_bbdd()
    cursor = conn.cursor()
    instruccion = f"DELETE FROM objetos WHERE nombre='{objeto.nombre}' AND personaje='{objeto.personaje}'"
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False