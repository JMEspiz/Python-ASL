#-*- coding: utf-8 -*-
from __future__ import print_function
import os


#Funciones para trabajar el archivo
def escribir_archivo(ruta2, msj, modo):
    f=open(ruta2, modo)
    msj2 = msj+"\n"
    f.write(msj2)
    f.close

def mostrar_archivo(ruta):
    f=open(ruta)
    
    for linea in f:
        print (linea)
    f.close()

def existe_archivo(ruta):
    if os.path.exists(ruta):
        print("Archivo encontrado, desea visualizarlo? [Y/N]")
        r1 = raw_input()
        if r1 == 'Y' or r1 == 'y':
            mostrar_archivo(ruta)
            #meter esto dentro de una funcion para DRY
            estado = True
            while(estado):
                print("Que desea hacer: \n1-Sobreescribir Archivo\n2-Anexar contenido\n3-Buscar otro archivo\n4-Salir del programa")
                r2 = raw_input()
                if r2 == "1":
                    modo = 'w'
                    print("Escriba el mensaje con el cual va a sobre escribir el archivo")
                    msj = raw_input()
                    escribir_archivo(ruta, msj, modo)
                    estado = False
                elif r2 == "2":
                    modo = 'a'
                    print("Escriba el mensaje con el cual va a sobre escribir el archivo")
                    msj = raw_input()
                    escribir_archivo(ruta, msj, modo)
                    print("Desea leer el archivo [Y/N]")
                    r5 = raw_input()
                    if r5 == 'Y' or r5 == 'y':
                        mostrar_archivo(ruta)
                    estado = False
                elif r2 == "4":
                    print("Programa finalizado")
                    estado = False
                elif r2 == "3":
                    estado = False
                    print("Ingrese el nombre del archivo")
                    ruta = raw_input()
                    existe_archivo(ruta)
                else:
                    print("Opcion no valida")
                    estado = True
    else:
        print("Archivo no encontrado.\nDesea crearlo [Y/N]")
        r3 = raw_input()
        if r3 == 'Y' or r3 == 'y':
            """print("Ingrese el nombre del archivo")
            nombre = raw_input()"""
            print("Ingrese el contenido")
            contenido = raw_input()
            modo = 'a+'
            escribir_archivo(ruta, contenido, modo)
            print("Desea leer el archivo [Y/N]")
            r5 = raw_input()
            if r5 == 'Y' or r5 == 'y':
                mostrar_archivo(ruta)
        else:
                print("Hola que hace")

#Logica del Programa
print("Ingrese el nombre del archivo")
ruta = raw_input()
existe_archivo(ruta)
