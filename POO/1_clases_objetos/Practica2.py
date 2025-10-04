'''
Ejercicio Practico #2 Modelar y Diagramar en POO 
'''
import os
os.system("cls")


#Clase de Coches
class Coches:
     #Metodo constructor que inicializa los valores cuando se instancia un objeto de la clase
    def __init__(self,color,marca,velocidad):
        self.__color=color #Atributos del objeto
        self.__marca=marca 
        self.__velocidad=velocidad

    #Métodos del objeto
    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad + incremento
        return self.__velocidad
     
    def frenar(self,decremento):
        self.__velocidad = self.__velocidad - decremento
        return self.__velocidad
    
    def tocarclaxon(self):
        print("Piiii")
    
#Instanciar o crear Objetos de la clase Coches
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)

print(f"Los valores del objeto 1 son {coche1.marca}, {coche1._color}, {coche1.__velocidad}")
print(f"El coche 1 acelero de: {coche1.__velocidad} a {coche1.acelerar(50)}")
print(f"Los valores del objeto 2 son {coche2.marca}, {coche2._color}, {coche2.__velocidad}")
print(f"El coche 2 freno de: {coche2.__velocidad} a {coche2.frenar(100)}")
