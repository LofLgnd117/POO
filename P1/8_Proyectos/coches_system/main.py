#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD
import os

def borrarPantalla():
   os.system("clear") 

def esperaTecla():
    input("\n\t... Oprima una tecla para continuar ...")   

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas

def resultados_insertar(respuesta):
    if respuesta==True:
        print("\n\tRegistro insertado correctamente en la BD")
    else:
        print("\n\tError al insertar el registro en la BD")
            
def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")

def menu_acciones(tipo):
    print(f"\n\t\t ::: Menu de acciones para {tipo} ::.\n\t1.- Insertar\n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar al menu principal")
    opcion=input("\tElige un opción: ").upper().strip()
    return opcion

def menu_autos():
    while True:
        borrarPantalla()
        menu_acciones("Autos")
        opcion=menu_acciones("Autos")
        if opcion=="1" or opcion=="INSERTAR":
            marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
            print("\n\tInsertar")
            esperaTecla()
                #Agregar en la BD
            auto=cochesBD.Autos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
            respuesta=auto.insertar()
            resultados_insertar(respuesta)
        elif opcion=="2" or opcion=="CONSULTAR":
            print("\n\tConsultar")
            borrarPantalla()
            registros= cochesBD.Autos.consultar()
            if len(registros)>0:
                num_autos=1
                for fila in registros:
                    print(f"Auto # {fila[0]} con ID: Marca: {fila[1]}, Color: {fila[2]}, Modelo: {fila[3]}, Velocidad: {fila[4]}, Caballaje: {fila[5]}, Plazas: {fila[6]}")
                    num_autos+=1
                    esperaTecla()
            else:
                print("\n\tNo hay registros de autos en la BD")
                esperaTecla()
                    
            esperaTecla()
        elif opcion=="3" or opcion=="actualizar":
            borrarPantalla()
            id= input("\n\tActualizar\n\tIngresa el ID del auto a actualizar: ")
            respuesta=cochesBD.Autos.consultar_id(id)
        elif opcion=="4" or opcion=="Eliminar":
            print("\n\Eliminar")
            esperaTecla()
        elif opcion=="5" or opcion=="Regresar al menu principal":
            break

def main():
   opcion=True
   while opcion:
    os.system("clear")
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            autos()
            esperaTecla()
        case "2":
            camionetas()
            esperaTecla()  
        case "3":
            camiones()
            esperaTecla()
        case "4":
            borrarPantalla()
            input("\n\t\tSalir del Sistema")
            opcion=False   
        case _:
            input("\n\tOpcion invalidad ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    main()

