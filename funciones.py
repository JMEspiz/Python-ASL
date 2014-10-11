#-*- coding:utf-8 -*-
#Impontado a print como una funcion
#con el __future__
# El + es una concatenacion y el la , es una concatenacion de tupla

from __future__ import print_function
def mi_funcion():
	print ("Hola Mundo")

a = mi_funcion()
print (a)

def nombres(nombre, apellido, edad):
	nombre_completo = "Mi nombre es %s %s y tengo %d" % (nombre, apellido, edad)
	print (nombre_completo)
nombres ("José", "Espinoza", 24)