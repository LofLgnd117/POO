from view.conexionBD import *

class Operaciones:
    @staticmethod
    def insertar(numero1, numero2, signo, resultado):
        try:
            cursor.execute(
                "INSERT INTO operaciones VALUES (NULL, NOW(), %s, %s, %s, %s)",
                (numero1, numero2, signo, resultado)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("Error insertar:", e)
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute("SELECT * FROM operaciones")
            return cursor.fetchall()
        except Exception as e:
            print("Error mostrar:", e)
            return []

    @staticmethod
    def actualizar(numero1, numero2, signo, resultado, id):
        try:
            cursor.execute(
                "UPDATE operaciones SET numero1=%s, numero2=%s, signo=%s, resultado=%s WHERE id=%s",
                (numero1, numero2, signo, resultado, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("Error actualizar:", e)
            return False

    @staticmethod
    def buscar(id):
        try:
            cursor.execute("SELECT * FROM operaciones WHERE id=%s", (id,))
            return cursor.fetchone()
        except Exception as e:
            print("Error buscar:", e)
            return None

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "DELETE FROM operaciones WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("Error eliminar:", e) 
            return False