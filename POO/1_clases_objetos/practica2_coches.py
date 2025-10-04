import os
os.system("cls")
"""
Ejercicio Practico 2 "Modelar y Diagramar en POO"
"""
class Coches:
    #Metodo constructor que inicializa los valores cuando se intancia un objeto de la clase
    def __init__(self,color,marca,velocidad):
        self.__color=color #atributo del objeto
        self.__marca=marca
        self.__velocidad=velocidad
    #Metodos del objeto
    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
    
    def frenar(self,decremento):
        self.__velocidad=self.__velocidad - decremento
        return self.__velocidad
    
    def tocar_claxon(self):
        print("PIIIIIIIIP")
    
#Instanciar o crear objetos de la clase Coches
coche1= Coches("Blanco", "toyota", 280)
coche2= Coches("Amarillo", "nissan", 180)

print(f"Los valores del objeto 1 son: {coche1.__marca}, {coche1.__color}, {coche1.__velocidad}")
print(f"El coche acelero de: {coche1.__velocidad} a {coche1.acelerar(50)}")
print(f"Los valores del objeto 2 son: {coche2.__marca}, {coche2.__color}, {coche2.__velocidad}")
print(f"El coche acelero de: {coche2.__velocidad} a {coche2.acelerar(100)}")
