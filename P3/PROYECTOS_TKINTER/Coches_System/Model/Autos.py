import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ConexionBD import conexion, cursor

class Autos:

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas

    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "INSERT INTO autos VALUES(null,%s,%s,%s,%s,%s,%s)"
            val = (marca, color, modelo, velocidad, caballaje, plazas)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error BD: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM autos")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def actualizar(id_auto, marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s"
            val = (marca, color, modelo, velocidad, caballaje, plazas, id_auto)
            cursor.execute(sql, val)
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def eliminar(id_auto):
        try:
            cursor.execute("DELETE FROM autos WHERE id=%s", (id_auto,))
            conexion.commit()
            return True
        except:
            return False