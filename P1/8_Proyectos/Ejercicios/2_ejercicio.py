'''
Realizar un programa en el se declaren dos valores enteros por teclado utilizando el metodo __init__.
Calcular despues la suma, resta, multiplicacion y division.
Utilizar un metodo para cada una e imprimir los resultados obtenidos.
llamar a la clase Calculadora.
'''
'''
class Calculadora:
    def __init__(self, entero1, entero2):
        self.entero1 = int(input("Numero 1: "))
        self.entero2 = int(input("Numero 2: "))

    def suma(self):
        return self.entero1 + self.entero2
    
    def resta(self):
        return self.entero1 - self.entero2
    
    def multiplicacion(self):
        return self.entero1 * self.entero2
    
    def division (self):
        return self.entero1 / self.entero2
#####################################################################################################################################
num1=int(input("Ingrese el primer valor entero: "))
num2=int(input("Ingrese el segundo valor entero: "))

Calcu= Calculadora(num1,num2)
print(f"\n\tEl resultado de la suma es: {Calcu.suma()}")
print(f"\n\tEl resultado de la resta es: {Calcu.resta()}")
print(f"\n\tEl resultado de la resta es: {Calcu.multiplicacion()}")
print(f"\n\tEl resultado de la resta es: {Calcu.division()}")
'''
class calculadora:
    def __init__ (self):
        self._numero1=int(input("Numero 1: "))
        self._numero2=int(input("Numero 2: "))

    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    def numero1(self, numero1):
        self.numero1 = numero1

    @property
    def numero2(self):
        return self._numero2
    @numero2.setter
    def numero2(self, numero2):
        self.numero2 = numero2

    def suma (self):
        return self._numero1 + self._numero2
    
    def resta (self):
        return self._numero1 - self._numero2
    
    def multiplicacion (self):
        return self._numero1 * self._numero2
    
    def division (self):
        return self._numero1 / self._numero2
    
operacion = calculadora()
print (f"{operacion.numero1} + {operacion.numero2} =  {operacion.suma()}")
print (f"{operacion.numero1} - {operacion.numero2} =  {operacion.resta()}")
print (f"{operacion.numero1} * {operacion.numero2} =  {operacion.multiplicacion()}")
print (f"{operacion.numero1} / {operacion.numero2} =  {operacion.division()}")
