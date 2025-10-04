import os
os.system("cls")

class Coches:

    #Atributos o propiedades(variables)
    #Caracteristicas del coche
    #Valores Iniciales
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0

#Crear los metodos setters y getters, estos modelos son importantes y necesarios
# en todas las clases que el programador interactue con los valores de los atributos a traves
# de estos metodos digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar
# un valor (set) a un atributo en particular de a clase a traves de un objeto
# Los metodos get siepre regresan valor, es decir el valor de la propiedad a traves del return
# Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getMarca(self):
        return self.__marca
    
    def setMarca(self,__marca):
        self.__marca=__marca

    def getColor(self):
        return self.__color
    
    def setColor(self,__color):
        self.__color=__color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,__modelo):
        self.__modelo=__modelo
    
    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,__velocidad):
        self.__velocidad=__velocidad
    
    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,__caballaje):
        self.__caballaje=__caballaje
    
    def getPlazas(self):
        return self.__plazas

    def setPlazas(self,__plazas):
        self.__plazas=__plazas

#Metodos o acciobes o funciones que hace el objeto
    def acelerar(self):
        pass

    def frenar(self):
        pass


#Crea un objeto o instancia de la clase Coches
coche1=Coches()
#Utiliza los metodos set para darle valores a las propiedades o atributos del objeto coche1
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
#Utiliza los metodos get para obtener los valores de las propiedades o atributos del objeto coche1
print(f'''
Marca: {coche1.getMarca()}
Color: {coche1.getColor()}
Modelo: {coche1.getModelo()}
Velocidad: {coche1.getVelocidad()}
Caballaje: {coche1.getCaballaje()}
Plazas: {coche1.getPlazas()}
''')

coche2=Coches()
coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

print(f'''
Marca: {coche2.getMarca()}  
Color: {coche2.getColor()}
Modelo: {coche2.getModelo()}
Velocidad: {coche2.getVelocidad()}
Caballaje: {coche2.getCaballaje()}
Plazas: {coche2.getPlazas()}
''')

