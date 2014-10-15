#-*- coding: utf-8 -*-
from decorador2 import logger

@logger
def sigma(*args):
	return sum([i for i in args])