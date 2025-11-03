from estudiante import estudiante
import os

class App:
    def __init__(self):
        self.main()
    
    def borrarPantalla(self):
        os.system('cls')

    def esperarTecla(self):
        input("\n\t\t Presione Enter para continuar...")

    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresa los siguientes datos del vehículo de tipo: '{tipo}' ...")
        marca=input("Marca: ").upper()
        color=input("Color: ").upper()
        modelo=input("Modelo: ").upper()
        velocidad=int(input("Velocidad: "))
        potencia=int(input("Potencia: "))
        plazas=int(input("Plazas: "))
        return marca,color,modelo,velocidad,potencia,plazas

    def menu_acciones(self,tipo):
        pass

    def respuesta_sql(self,respuesta):
        pass

    def menu_estudiante(self):
        pass

    def main(self):
        pass


if __name__ == "__main__":
    app=App 
    