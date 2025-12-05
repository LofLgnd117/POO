import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ConexionBD import conexion, cursor

class Camionetas:
    
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            es_cerrada = 1 if cerrada else 0 
            sql = "INSERT INTO camionetas VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas, traccion, es_cerrada)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error BD: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(id_cam, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            es_cerrada = 1 if cerrada else 0
            sql = "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s"
            val = (marca, color, modelo, velocidad, caballaje, plazas, traccion, es_cerrada, id_cam)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_cam):
        try:
            cursor.execute("DELETE FROM camionetas WHERE id=%s", (id_cam,))
            conexion.commit()
            return True
        except:
            return False