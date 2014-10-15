#-*- coding: utf-8 -*-
from __future__ import print_function

print("Ingrese la direccion del archivo con la que desee trabajar")
ruta = raw_input()
print("Ingrese el texto que desea agregar")
msj = raw_input()

def escribir_archivo(ruta2, msj):
	f=open(ruta2, 'a+')
	f.write(msj)


def mostrar_archivo(ruta):
    f=open(ruta)
    
    for linea in f:
        print (linea)
    f.close()


escribir_archivo(ruta, msj)

print("desea leer el archivo? [Y/N]")
resp = raw_input()

if resp == 'Y' or resp == 'y':
	mostrar_archivo(ruta)
else:
	print("Ola k ase")