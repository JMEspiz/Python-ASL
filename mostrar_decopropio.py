#-*- utf-8 -*-
from decopropio import deco

@deco
def conversor(*args):
    for arg in args:
        ps = arg *326.425
        dls = arg * 0.15
        a = "Monto en Pesos: %.2f  Monto en Dolares: %.2f" % (round(ps,2), round(dls,2))
        print a