#-*- coding: utf-8 -*-
#from __future__ import print_function
#import urllib

print"Bienvenido indique la ruta al archivo"
ruta = raw_input()

def mostrar_archivo(ruta2):
    f=open(ruta2)
    
    for linea in f:
        print linea
    f.close()

mostrar_archivo(ruta)