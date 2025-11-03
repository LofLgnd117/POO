#Enacpsular, es un pilar de la poo que permite indicar cual es la manera de como poder utilizar los atributos y metodos de una clase
#a la hora de usar en objetos o en herencia
import os
os.system("cls")

class Clase:
    atributo_publico = "Soy un atributo publico"
    _atributo_protegido = "Soy un atributo protegido"
    __atributo_privado = "Soy un atributo privado"

    def __init__(self, color, tamanio):
        self.__color = color
        self.__tamanio = tamanio

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color = color

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    @property
    def atributopublico(self):
        return self.atributo_publico
    
    @atributopublico.setter
    def atributopublico(self, atributo_publico):
        self.atributo_publico = atributo_publico

    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    
    @atributo_protegido.setter
    def atributo_protegido(self, atributo_protegido):
        self._atributo_protegido = atributo_protegido
    
    @property
    def __atributo_privado(self):
        return self.__atributo_privado
    
    @__atributo_privado.setter
    def __atributo_privado(self, __atributo_privado):
        self.__atributo_privado = __atributo_privado

#Utilizar la clase

objeto=Clase("Rojo","Grande")
#print(objeto._atributo_protegido) No es una buena practica
#print(objeto.__atributo_privado) #Error, no se puede acceder al atributo privado

print(objeto.atributopublico)
print(objeto._atributo_protegido)
print(objeto.__atributo_privado)
objeto.color="Amarillo"
