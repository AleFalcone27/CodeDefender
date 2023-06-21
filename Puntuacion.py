import sqlite3
import datetime
import pygame


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
    except:
        pass

def crear_registro(nombre_jugador,score,tiempo):
    with sqlite3.connect("putuacion.db") as conexion:
        conexion.execute("INSERT INTO tabla_puntuacion (nombre,puntuacion,tiempo,fecha) values (?,?,?,?)", (nombre_jugador,score,tiempo,datetime.date.today()))
        print("-PUNTUACION CARGADA-")



def obtener_tabla_de_puntuaciones(screen):
    pos = 75
    with sqlite3.connect("putuacion.db") as conexion:
        cursor = conexion.execute("SELECT nombre, puntuacion, tiempo , fecha FROM tabla_puntuacion order by puntuacion DESC")
        escribir_titulo(screen)
        for fila in cursor:
            fila_sanitizada = sanitizar_registro(fila)
            pos = pos + 25
            font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 20)
            fila_sanitizada = font.render(fila_sanitizada, True, "BLACK")


            screen.blit(fila_sanitizada, (100, pos))  
            pygame.display.flip()
        
        
        cursor.execute("SELECT COUNT(*) FROM tabla_puntuacion")
        cantidad_registros = cursor.fetchone()[0]
        if cantidad_registros > 10:
            eliminar_registros()


def eliminar_registros():
    with sqlite3.connect("putuacion.db") as conexion:
        try: 
            conexion.execute("DELETE FROM tabla_puntuacion WHERE puntuacion < 30")
            print("-SE ELIMINARON AQUELLAS PUNTUACIONES MENORES A 30-")
        except: 
            print("--ERROR EN LA LIMPIEZA--")


def sanitizar_registro(fila):
    elementos = [str(elemento).strip('\'\"') for elemento in fila]
    lista = ' - '.join(elementos)
    return lista


def escribir_titulo(screen):
    font1 = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 25)
    font2 = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 20)
    text = "TABLA DE PUNTUACIONES"
    text2 = "NOMBRE - SCORE - TIME - FECHA"
    text = font1.render(text , True, "BLACK")
    text2 = font2.render(text2 , True, "BLACK")
    
    screen.blit(text, (100,25))
    screen.blit(text2, (100,75))
    
    
        # nombre,score,tiempo = fila
        # linea = nombre, score, tiempo 
        # linea = str(linea)
        # linea.replace("''"," ")
        # linea = linea.replace("("," ")
        # linea = linea.replace(")"," ")