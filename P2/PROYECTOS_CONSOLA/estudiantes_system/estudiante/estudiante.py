from conexionBD import *

class Estudiante():
    def __init__(self,nombre,nota):
        self._nota = nota
        self._nombre = nombre
    
    @property
    def nombre (self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def nota (self):
        return self._nota
    @nota.setter
    def nota(self,nota):
        self._nota = nota

    def imprimir(self):
        print(f"El nombre del Estudiante es: {self.nombre} y saco {self.nota}")

    def mostrar(self):
        if self.nota>=7:
            return "Si Aprobo"
        else:
            return "No aprobo"
            
    @staticmethod
    def insertar(nombre,nota):
        try:
          cursor.execute(
            "insert into estudiantes values(null,%s,%s)",
            (nombre,nota)
        )
          conexion.commit()
          return True
        except:
          return False

    @staticmethod
    def consultar():
        pass

    @staticmethod
    def actualizar(nombre,nota,id):
        pass

    @staticmethod
    def eliminar(id):
        pass
