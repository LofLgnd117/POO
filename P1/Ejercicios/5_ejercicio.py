class Universidad:
    def __init__(self, nombre_uni):
        self.nombre_uni = nombre_uni

        @property
        def nombre_uni(self):
            return self.nombre_uni
        
        @nombre_uni.setter
        def nombre_uni(self, nombre_uni):
            self.nombre_uni = nombre_uni

class Carrera:
    def __init__(self, especialidad):
        self._especialidad = especialidad

        @property
        def especialidad(self):
            return self.especialidad
        
        @especialidad.setter
        def especialidad(self, especialidad):
            self.especialidad = especialidad
class Estudiante(Carrera, Universidad):
        def __init__(self, edad, nombre, nombre_uni, especialidad):
            self._edad = edad
            self._nombre = nombre
            Universidad.__init__(self, nombre_uni)
            Carrera.__init__(self, especialidad)
        @property

        def nombre(self):
            return self._nombre
        def edad(self):
            return self._edad
        
        @nombre.setter
        def nombre(self, nombre):
            self._nombre = nombre
        @edad.setter
        def edad(self, edad):
            self._edad = edad

persona = Estudiante("Ruben Aguirre", 120, "UTD", "T.I.")
print(f"El estudiante {persona.nombre} de {persona.edad} años, estudia la carrera de {persona._especialidad} en la universidad {persona.nombre_uni}.")