#-*- coding: utf-8 -*-
def conversor(*args):
    for arg in args:
        ps = arg *326.425
        dls = arg * 0.15
        a = "Monto en Pesos: %.2f  Monto en Dolares: %.2f" % (round(ps,2), round(dls,2))
        print a
        
            

def deco(fn):
    def wrapper(*args):
        for i, arg in enumerate(args):
            print "El resultado del movimiento %s ingresado en Bolivares: %s" % (i, arg)
        return fn(*args)
    return wrapper
