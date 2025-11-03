from conexionBD import *

class Notas:
  @staticmethod
  def crear(_usuario_id,_titulo,_descripcion):
    try:
      cursor.execute(
      "insert into notas values(null,%s,%s,%s,NOW())",
      (_usuario_id,_titulo,_descripcion)
      )
      conexion.commit()
      return True
    except:
      return False

  @staticmethod
  def mostrar(_usuario_id):
    try:
      cursor.execute(
      "select * from notas where usuario_id=%s",
      (_usuario_id,)
      )
      return cursor.fetchall()
    except:    
      return []
    
  @staticmethod
  def actualizar(id,_titulo,_descripcion):
    try:
      cursor.execute(
      "update notas set titulo=%s,descripcion=%s where id=%s",
      (_titulo,_descripcion,id)
      )
      conexion.commit()
      return True
    except: 
       return False
    
  @staticmethod
  def eliminar(id):
    try:
      cursor.execute(
        "delete from notas where id=%s",
        (id,)
      )
      conexion.commit()
      return True
    except:
      return False
          
