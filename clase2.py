#-*- coding: utf-8 -*-
from __future__ import print_function

class Auto(object):

	gasolina = 0
	

	def __init__(self, gasolina):
		Auto.gasolina = gasolina
		

	@classmethod
	def encender(cls, gasolina):		
		if gasolina > 0:
			print("Carro encendido")
		else:
			print("No enciende, verifique gasolina")

	@staticmethod
	def mover(gasolina):
		if gasolina > 0:
			print("Estas en movimiento")
			gasolina = gasolina -1
		else:
			print("El carro no se mueve")
