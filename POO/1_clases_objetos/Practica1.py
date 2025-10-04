import os
os.system("cls")


#EStructurado
def area(base, altura):
    return (base * altura) / 2

#POO

class AreaRectangulo:
    def __init__(self,b,a):
            self.base=b
            self.altura=a

    def areaRectangulo(self,base, altura):
        area = base * altura
        return area
    


rectangulo=AreaRectangulo()
print(rectangulo.areaRectangulo(5,6))