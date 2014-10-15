#-*- coding: utf-8 -*-
from __future__ import print_function

class Archivo():

	def __init__(self, nombre):
		self.nombre = nombre

	def existe(nombre):
		if os.path.exists(nombre):
			return True
		else:
			return False

	def leer(nombre):
		nombre = open(nombre)
		for linea  in nombre:
			print(linea)
		nombre.close()

	def escribir(nombre, msj, modo2):
		nombre= open(nombre, modo2)
		nombre.write(msj)
		nombre.close()

	def modo(nombre, msj, modo):
		if modo == 1:
			modo2 = 'w'
			escribir(nombre, msj, modo2)
		elif modo == 2:
			modo2 = 'a'
			escribir(nombre, msj, modo2)
		else:
			print("Error modo no admitido")



		

