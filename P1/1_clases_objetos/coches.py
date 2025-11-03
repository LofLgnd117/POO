import os
os.system("cls")

class Coches:
    #Atributos o propiedades(variables)
    #Caracteristicas del coche
    #Valores Iniciales
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0

    def acelerar(self):
        pass

    def frenar(self):
        pass



coche1=Coches()
coche1.marca="VM"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

coche2=Coches()
coche2.marca="Nissasn"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6



print(f"La marca es: {coche1.marca} \n\tEl color es: { coche1.color} \n\tEl modelo es: {coche1.modelo} \n\tLa velocidad es: {coche1.velocidad} \n\tEl caballaje es: {coche1.caballaje} \n\tLas plazas son: {coche1.plazas}")
print(f"La marca es: {coche2.marca} \n\tEl color es: { coche2.color} \n\tEl modelo es: {coche2.modelo} \n\tLa velocidad es: {coche2.velocidad} \n\tEl caballaje es: {coche2.caballaje} \n\tLas plazas son: {coche2.plazas}")