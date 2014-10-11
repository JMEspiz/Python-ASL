# -*- coding:utf-8 -*-
dinero = 500
objeto1 = 152
objeto2 = 234
objeto3 = 159

print "Bienvenido listo para comprar, su dinero dispoble es: ", int(dinero)

if objeto1 < dinero:
    print "Has comprado una cobarta"
    dinero = dinero - objeto1
else: 
    print "Dinero insuficiente"

print "Dinero Disponible: ", int(dinero)

if objeto2 < dinero:
    print "Has comprado una camisa"
    dinero = dinero - objeto2
else:
    print "Dinero insuficiente"

print "dinero disponible", int(dinero)

if objeto3 < dinero:
    print "Has comprado un pantalon"
    dinero = dinero - objeto3
else:
    print "No tiene suficiente dinero"
