import os
os.system("cls")
"""
Ejercicio Practico 2 "Modelar y Diagramar en POO"
"""
class Coches:
    #Metodo constructor que inicializa los valores cuando se intancia un objeto de la clase
    def __init__(self,color,marca,velocidad):
        self.color=color #atributo del objeto
        self.marca=marca
        self.velocidad=velocidad
    #Metodos del objeto
    def acelerar(self,incremento):
        self.velocidad=self.velocidad+incremento
        return self.velocidad
    
    def frenar(self,decremento):
        velocidad=velocidad - decremento
        return velocidad
    
#Instanciar o crear objetos de la clase Coches
coche1= Coches("Blanco", "toyota", 280)
coche2= Coches("Amarillo", "nissan", 180)

print(f"Los valores del objeto 1 son: {coche1.marca}, {coche1.color}, {coche1.velocidad}")
print(f"El coche acelero de: {coche1.velocidad} a {coche1.acelerar(50)}")
print(f"Los valores del objeto 2 son: {coche2.marca}, {coche2.color}, {coche2.velocidad}")
print(f"El coche acelero de: {coche2.velocidad} a {coche2.acelerar(100)}")
