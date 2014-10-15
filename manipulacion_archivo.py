#-*- coding: utf-8 -*-
from __future__ import print_function

archivo = open("archivo.txt")
for linea in archivo:
	print linea

archivo.close()
