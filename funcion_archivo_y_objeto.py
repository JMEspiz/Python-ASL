
from __future__ import print_function
import os
from archivo import Archivo


print("Bienvenido al manejador de archivos: \nIngrese el nombre del archivo")
r1 = raw_input()

archivo = Archivo(r1)

if archivo.existe(archivo):
	print("Archivo encontrado, desea visualizarlo? [Y/N]")
	r2 = raw_input()
	if r2 == 'Y' or r2 == 'y':
		archivo.leer(archivo)
		print("Que desea hacer:\n1 - Sobreescribir\n 2 - Anexar")
		rmodo = raw_input()
		if rmodo == 1:
			print("Ingrese el contenido")
			msj = raw_input()
			archivo.modo(nombre, msj, rmodo)
		elif rmodo == 2:
			print("Ingrese el contenido")
			msj = raw_input()
			archivo.modo(nombre, nombre, rmodo)
	else:
		print("Archivo no encontrado, desea generarlo? [Y/N]")
		r3 = raw_input()
		if r3 == 'Y' or r3 == 'y':
			print("Ingrese el contenido")
			msj = raw_input()
			modo2 = 'w'
			archivo.modo(archivo, msj, modo2)
		else:
			print("Proceso finalizado")


