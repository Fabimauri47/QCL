import matriz_Complejos as ls
import math


def amplitud_Transicional(matrix1,matriz2):
    temporal = ls.matrizmultiplication(matrix1,ls.Transpusta_matrices(ls.matriz_conjugada(matrix2)[0]))


    var1  = 0
    var2 = 0

    for i in range(len(temporal):
        var1+=float("%.4f" % (temporal[0][0][0]));var2+=float("%.4f" % (temporal[0][0][1]))


    return (var1,var2)


                   
               
