"""
Practica 1# Implementar paradigma estructurado VS OO 
Crear un programa que obtenga el area de un rectangulo
"""

#1.- Estrucuturado
base = 5
altura = 6
def arearectangulo():
    area= base * altura
    return area
print(f"El area del rectangulo es: {arearectangulo(5,6)}")

#2.- OO

class AreaRectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def areaRectangulo(self):
        area = self.base * self.altura
        return area
rectangulo = AreaRectangulo(5,6) #instanciar un objeto de la clase AreaRectangulo

print(f"El area del rectangulo es: {rectangulo.areaRectangulo()}")
