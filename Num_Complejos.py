from sys import stdin
import math


def suma(c1,c2):
    pReal = c1[0]+ c2[0]
    pImag = c1[1] + c2[1]

    return pReal,pImag

def resta(c1,c2):
    pReal = c1[0]- c2[0]
    pImag = c1[1] - c2[1]

    return pReal,pImag


def multiplicacion(c1,c2):
    pReal = c1[0] * c2[0] - c1[1] * c2[1]
    pImag = c1[0] *c2[1] + c1[1] * c2[0]
    return pReal,pImag

def division(c1,c2):
    pReal = (c1[0] * c2[0] + c1[1]* c2[1]) / ((c2[0]**2) + (c2[1]**2))
    pImag = (c2[0] * c1[1] - c1[0]* c2[1]) / ((c2[0]**2) + (c2[1]**2))

    return pReal, pImag

def modulo(c1):
    mod = ((c1[0]**2) + (c1[1]**2))**0.5
    return mod

def conjugado(c1):
    conjugado = c1
    conjugado[1] *= -1
    return conjugado

def cartesiono_A_polares(c1):
    pReal=(((c1[0])**2)+((c1[1])**2))**0.5
    pImag= math.atan(c1[1]/c1[0])
    return pReal,math.degrees(pImag)

def polar_A_cartesiano(c1):
    pReal=(c1[0]*math.cos(c1[1]))
    pImag=(c1[0]*math.sin(c1[1]))
    return pReal,pImag

def fase(c1):
    ANGULO=math.atan(c1[1]/c1[0])
    return math.degrees(ANGULO)


##def main():
##    c1 = [float(x)for x in stdin.readline().strip().split()]
##    c2 = [float(x)for x in stdin.readline().strip().split()]
##    c3= (0,1)
##
##    sumar = suma(c1,c2)
##    restar = resta(c1,c2)
##    multiplicar = multiplicacion(c1,c2)
##    dividir = division(c1,c2)
##    modulacion = modulo(c1,c2)
##    conjugacion = conjugado(c1,c2)
##    cartesiano_polar = cartesiono_A_polares(c1,c2)
##    polar_cartesiano = polar_A_cartesiano(c1,c2)
##    fases = fase(c1,c2)
##    print("Sumar = {0} + {1}i".format(sumar[0],sumar[1]))
##    print("Restar = {0} + {1}i".format(restar[0],restar[1]))
##    print("Multiplicacion = {0} + {1}i".format(multiplicar[0],multiplicar[1]))
##    print("Dividir = {0} + {1} i ".format(dividir[0],dividir[1]))
##    print("Modulo = {0} ".format(modulacion))
##    print("Conjugado = {0} + {1} i ".format(conjugacion[0],conjugacion[1]))
##    print("cartesiano_a_polar = {0} + {1} i ".format(cartesiano_polar[0],cartesiano_polar[1]))
##    print("polar_a_cartesiano = {0} + {1} i ".format(polar_cartesiano[0],polar_cartesiano[1]))
##    print("Conjugado = {0} + {1} i ".format(conjugacion[0],conjugacion[1]))

#main()
