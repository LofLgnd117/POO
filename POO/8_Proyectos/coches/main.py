from coches import Coches, Camiones, Camionetas
import os
os.system("cls")
'''
coche= Coches("VW", "Blanco", "2020", 220, 200, 5)
print(coche.marca, coche.color, coche.modelo, coche.velocidad, coche.caballaje, coche.plazas)

camioneta = Camionetas("Chevrolet", "Rojo", "2021", 250, 220, 5, "4x4", "Gasolina")
print(camioneta.marca, camioneta.color, camioneta.modelo, camioneta.velocidad, camioneta.caballaje, camioneta.plazas, camioneta.traccion, camioneta.cerrada)

camiones = Camiones("Volvo", "Blanco", "2023", 400, 180, 2, 4, "10 Toneladas")
print(camiones.marca, camiones.color, camiones.modelo, camiones.velocidad, camiones.caballaje, camiones.plazas, camiones.ejes, camiones.capacidad)'''
opcion = True
while opcion:
    opcion = input("\n\t\t Menu de Vehiculos \n\n 1. Coches \n 2. Camionetas \n 3. Camiones \n 4. Salir \n\n Elige una opcion: ")
    match opcion:
        case "1":
            print("Autos")
            input("Presiona una tecla para continuar...")
        case "2":
            print("Camionetas")
            input("Presiona una tecla para continuar...")
        case "3":
            print("Camiones")
            input("Presiona una tecla para continuar...")
        case "4":
            print("Saliendo...")
            input("Presiona una tecla para continuar...")
            opcion = False
        case _:
            print("Opcion no valida")
            input("Presiona una tecla para continuar...")