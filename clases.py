#-*- codig: utf-8 -*-
from __future__ import print_function

class Auto:
	#Abstraccion a objeto de un Auto
	def __init__(self, gasolina):
		self.gasolina = gasolina
		self.estado = False
		print ("tenemos %d litros" % self.gasolina)

	def arrancar(self):
		if self.gasolina > 0:
			print("Carro Encendido")
			self.estado = True
		else:
			print("No Arranca")
			self.estado = False

	def conducir(self):
		if self.gasolina > 0 and self.estado==True:
			self.gasolina -= 1
			print("Esta en movimiento. Quedan %d litros" % self.gasolina)
		elif self.estado == False:
			print ("El carro no esta encendido, debe encenderlo para conducir")
		elif self.gasolina <= 0:
			print ("El carro no se mueve, sin gasolina")

	def apagar(self):
		self.estado= False
		print ("Has apagado el carro")

	def verificargas(self):
		if self.gasolina < 5 and self.gasolina > 0:
			print ("Le comendamos dirigirse a una estacion de gasolina a la brevedad, su nivel es %d" % self.gasolina)
		elif self.gasolina <= 0:
			print ("No tiene gasolina.. A empujar brother")
		else:
			print("Su nivel actual de gasolina es de: %d" % self.gasolina)



"""mi_auto = Auto(5)
mi_auto.arrancar()
mi_auto.conducir()
mi_auto.apagar()
mi_auto.conducir()
mi_auto.verificargas()
mi_auto.arrancar()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.verificargas()"""
