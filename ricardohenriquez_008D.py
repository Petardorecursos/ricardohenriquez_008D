import csv
import os
import time
from random import *
pedidos = []
sectores = ("san bernardo","calera de tango","buin")
def menu():
    act = 1
    while act == 1:
        try:
            print("Bienvenido a CatPremiun tu empresa de repartos de confianza")
            print("_"*30)
            print("1-Registrar pedido")
            print()
            print("2-listar todos los pedidos")
            print()
            print("3-imprimir hoja de ruta")
            print()
            print("4-salir del programa")
            print("_"*30)
            print()
            opc = int(input("Ingrese su opcion: "))
            if opc >= 1 and opc <=4:
                act = 2
                os.system("cls")
                opciones(opc,pedidos)
        except ValueError:
            print("valor ingresado incorrecto")
            time.sleep(3)
            
        

def opciones(opc,pedidos):
    if opc == 1:
        os.system("cls")
        pedidos = []
        numeropedido = randint(1,100)
        nombre = input("ingrese su nombre:")
        print()
        apellido = input("ingrese su apellido:")
        print()
        comuna = input("ingrese su comuna:")
        print()
        direccion = input("direccion exacta:")
        os.system("cls")
        actt = 1
        while actt == 1:
            try:
                print("_"*30)
                print()
                print("1-Saco de 5Kg")
                print()
                print("2-Saco de 10Kg")
                print()
                print("3-Saco 20Kg")
                print()
                opcc = int(input("Ingrese su opcion: "))
                if opcc >= 1 and opcc <=3:
                    actt = 2
                    os.system("cls")
                    saquitos(opcc,numeropedido,nombre,apellido,comuna,direccion)
                elif opcc <1 or opcc >3:
                    print("opcion ingresada no valida, vuelva a intentarlo")
                    time.sleep(2)
            except ValueError:
                print("valor ingresado incorrecto")
                time.sleep(3)
    elif opc == 2:
        os.system("cls")
        print("cargando su historial de pedidos")
        time.sleep(3)
        print(pedidos)
    elif opc == 3:
        os.system("cls")
        hojaderuta(sectores,pedidos)
    else :
        os.system("cls")
        time.sleep(2)
        print("saliendo de nuestra tienda en linea")   
        print("todos sus pedidos estaran guardados en el siguiente archivo: pedidos.csv")

        
        
        
def saquitos(opcc,numeropedido,nombre,apellido,comuna,direccion):
    if opcc == 1:
        act2 = 1
        ed = 0
        while act2 == 1:
            try:
                need = int(input("ingrese la cantidad de sacos de 5 kg que necesita"))
                if need >=1:
                    sacos5kg = need + ed
                    act2 = 2
                    os.system("cls")
                    print("registrando pedido...")
                    time.sleep(2)
                    print("_"*30)
                    print("Nro.ped: ",numeropedido)
                    print("cliente: ",nombre,"",apellido)
                    print("direccion: ",direccion)
                    print("sector o comuna: ",comuna)
                    print("sacos 5Kg:", sacos5kg)
                    print("_"*30)
                    numeropedido += 1
                    listanew = [numeropedido, nombre,apellido,direccion,comuna,"sacos 5kg: ",sacos5kg]


                        

                elif need<1:
                    print("el minimo de sacos para poner en su carrito: 1")
            except ValueError:
                print("valor ingresado incorrecto")
                time.sleep(3)
    if opcc == 2:
        act2 = 1
        ed = 0
        while act2 == 1:
            try:
                need = int(input("ingrese la cantidad de sacos de 10 kg que necesita"))
                if need >=1:
                    sacos10kg = need + ed
                    act2 = 2
                    os.system("cls")
                    print("registrando pedido...")
                    time.sleep(2)
                    print("_"*30)
                    print("Nro.ped: ",numeropedido)
                    print("cliente: ",nombre,"",apellido)
                    print("direccion: ",direccion)
                    print("sector o comuna: ",comuna)
                    print("sacos 10Kg:", sacos10kg)
                    print("_"*30)
                    numeropedido += 1
                    listanew = [numeropedido, nombre,apellido,direccion,comuna,"sacos 5kg: ",sacos5kg]


                    

                elif need<1:
                    print("el minimo de sacos para poner en su carrito: 1")
            except ValueError:
                print("valor ingresado incorrecto")
                time.sleep(3)
    if opcc == 3:
        act2 = 1
        ed = 0
        while act2 == 1:
            try:
                need = int(input("ingrese la cantidad de sacos de 20 kg que necesita"))
                if need >=1:
                    sacos20kg = need + ed
                    os.system("cls")
                    print("registrando pedido...")
                    time.sleep(2)
                    print("_"*30)
                    print("Nro.ped: ",numeropedido)
                    print("cliente: ",nombre,"",apellido)
                    print("direccion: ",direccion)
                    print("sector o comuna: ",comuna)
                    print("sacos 20Kg:", sacos20kg)
                    print("_"*30)
                    numeropedido += 1
                    listanew = [numeropedido, nombre,apellido,direccion,comuna,"sacos 5kg: ",sacos5kg]


                elif need<1:
                    print("el minimo de sacos para poner en su carrito: 1")
            except ValueError:
                print("valor ingresado incorrecto")
                time.sleep(3)
                
def hojaderuta(sectores,pedidos):
    hd = 1
    while hd == 1:
        try:
            sectoris = input("ingrese sector a enviar el pedido")
            activado = sectoris in sectores
            if activado == True:
                    with open("hojitaderuta.txt","w") as file1:
                        file1.write(pedidos)
                        time.sleep(2)
                        print("el archivo a sido guardado correctamente")
                        time.sleep(2)
                        print("abriendo el archivo")
                        time.sleep(1)
                        abrirarchivotxt() 
                
            elif activado == False:
                print("no podemos hacer envios a su sector, Gracias por su atencion")
                hd = 2
        except ValueError:
            print("datos ingresados no validos")
            time.sleep(3)
            

        
def abrirarchivotxt():
    archivo = open("hojitaderuta.txt","r")
    print(archivo.read())
    
        
        
menu()
