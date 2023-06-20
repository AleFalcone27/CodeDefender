import sqlite3

nombre_jugador = "Alejo"
score = 34
tiempo = 100
fecha = "20/6/23"

# def guardar_puntuacion()

with sqlite3.connect("putuacion.db") as conexion:
    try: 
        sentencia = """ create table tabla_puntuacion
        (
        id integer primary key autoincrement,
        nombre text, 
        puntuacion int,
        tiempo int,
        fecha text
        )
        """
    
        conexion.execute(sentencia)
        print("Se creo la tabla_puntuacion")
    except sqlite3.OperationalError:
        pass
        
# def crear_registro():
    
    # conexion.execute("INSERT INTO tabla_puntuacion (nombre,puntuacion,tiempo,fecha) values (?,?,?,?)", (nombre_jugador,score,tiempo,fecha))
    # print("-REGISTRO CARGADO-")
    
        
        
        
# def obtener_tabla_de_puntuaciones():
    cursor = conexion.execute("SELECT * FROM tabla_puntuacion order by puntuacion ASC")
    jugador = list()
    for fila in cursor:
        print(fila)
        


# mostrar_tabla_de_puntuaciones()