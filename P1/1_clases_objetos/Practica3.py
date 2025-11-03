import os
os.system('cls')

# Profesores

class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia = experiencia

    @property
    def num_profesor(self):
        return self.__num_profesor
    @num_profesor.setter
    def num_profesor(self, num_profesor):
        self.__num_profesor = num_profesor

    def impartir(self):
        pass

    def evaluar(self):
        pass

# Alumnos

class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def estudiar(self):
        pass

    def inscribirse(self):
        pass

# Cursos

class Cursos:
    def __init__(self, nombre, codigo, creditos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def creditos(self):
        return self.__creditos
    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos

    def asignar(self):
        pass

# OBJETOS PROFESORES
profesor1 = Profesores("Juan", 15, 34)
profesor2 = Profesores("Ruben", 17, 37)

print(f"{profesor1.nombre},{profesor1.experiencia},{profesor1.num_profesor}")
print(f"{profesor2.nombre},{profesor2.experiencia},{profesor2.num_profesor}")

# OBJETOS ALUMNOS
alumno1 = Alumnos("Ana", 20, "A001")
alumno2 = Alumnos("Luis", 22, "A002")

print(f"{alumno1.nombre},{alumno1.edad},{alumno1.matricula}")
print(f"{alumno2.nombre},{alumno2.edad},{alumno2.matricula}")

# OBJETOS CURSOS
curso1 = Cursos("Matemáticas", "MAT101", 8)
curso2 = Cursos("Historia", "HIS201", 6)

print(f"{curso1.nombre},{curso1.codigo},{curso1.creditos}")
print(f"{curso2.nombre},{curso2.codigo},{curso2.creditos}")