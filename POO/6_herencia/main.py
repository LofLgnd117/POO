#Instanciar los Objetos para posteriormente implementarlos.
from coches import Coches,Camines, Camionetas

coche=Coches("VW","Blanco","202",220,200,5)
print(coche.marca, coche.acelerar())

camioneta=Camionetas("Chevrolet","Rojo","2020",180,150,7,"Tracera",True)
print(camioneta.marca, camioneta.acelerar())

camion=Camines("Ford","Azul","2019",160,120,3,2,5000)
print(camion.marca, camion.acelerar())

# num_coches=int(input("¿Cuantos coches deseas?: "))

#for i in range(0,num_coches):
#    print(f"\n\t...Datos del Coche...{i+1}")
#    marca=input("Ingrese la marca del coche: ").upper()
#    color=input("Ingrese el color del coche: ").upper()
#    modelo=input("Ingrese el modelo del coche: ").upper()
#    velocidad=int(input("Ingrese la velocidad maxima del coche: "))
#    potencia=int(input("Ingrese el caballaje del coche: "))
#    plazas=int(input("Ingrese el numero de plazas del coche: "))
#
#    #Crea un objeto o instancia de la clase Coches
#
#    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)
#
#    print(f"Datos del Vehiculo \n Marca: {coche1.marca()} \n Color: {coche1.color()} \n Modelo: {coche1.modelo()} \n Velocidad Maxima: {coche1.velocidad()} \n Caballaje: {coche1.caballaje()} \n Numero de Plazas: {coche1.plazas()}")
#
#    print(f"\n\n\t {coche1.acelerar()}")