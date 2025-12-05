import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ConexionBD import conexion, cursor

class Camiones:

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            sql = "INSERT INTO camiones VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error BD: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(id_cam, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        try:
            sql = "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, eje=%s, capacidadCarga=%s WHERE id=%s"
            val = (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadCarga, id_cam)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_cam):
        try:
            cursor.execute("DELETE FROM camiones WHERE id=%s", (id_cam,))
            conexion.commit()
            return True
        except:
            return False