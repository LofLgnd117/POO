import os
os.system("cls")

#Con este metodo se inicializa un objeto cuando es creado con valores iniciales
class Coches:
    _marca = ""
    _color = ""
    _modelo = ""
    _velocidad = 0
    _caballaje = 0
    _plazas = 0

    #2da forma de crear los metodos getters y setters
    @property
    def marca(self): 
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def caballaje(self):
        return self._caballaje
    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje = caballaje

    @property
    def plazas(self):
        return self.plazas
    @plazas.setter
    def plazas(self, plazas):
        self._plazas = plazas


    #Metodos
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Camiones(Coches):
    def __init__(self, marca, color, modelo, caballaje, velocidad, plazas, ejes, capacidad):

        super().__init__(marca, color, modelo, caballaje, velocidad, plazas, ejes, capacidad)
        self.__ejes = ejes
        self.__capacidad = capacidad
    @property
    def ejes(self):
        return self.__ejes
    @ejes.setter
    def ejes(self, ejes):
        self.__ejes = ejes
    @property
    def capacidad(self):
        return self.__capacidad
    @capacidad.setter
    def capacidad(self, capacidad):
        self.__capacidad = capacidad

    #metodos
    def transportar(self, peso):
        self.peso = peso
        return self.peso
    
    

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, caballaje, velocidad, plazas, traccion, cerrada):

        super().__init__(marca, color, modelo, caballaje, velocidad, plazas, traccion, cerrada)
        self.__traccion = traccion
        self.__cerrada = cerrada
    @property
    def traccion(self):
        return self.__traccion
    @traccion.setter
    def traccion(self, traccion):
        self.__traccion = traccion
    @property
    def cerrada(self):
        return self.__cerrada
    @cerrada.setter
    def cerrada(self, cerrada):
        self.__cerrada = cerrada
    
    #metodos
    def transportar(self, num_pasarejeros):
        self.num_pasarejeros = num_pasarejeros
        return self.num_pasarejeros