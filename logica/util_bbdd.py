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
                car integer 
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
                   f"{personaje.caracteristicas["DES"]}, {personaje.caracteristicas["CAR"]}"
                   f")")
    try:
        cursor.execute(
            instruccion
        )
        conn.commit()
        return True
    except sql.IntegrityError:
        conn.close()
        return False

def leer_personajes():
    conn = conectar_bbdd()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM personajes"
    )
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    return resultado


if __name__ == "__main__":
    # crear_tabla_personajes()
    leer_personajes()