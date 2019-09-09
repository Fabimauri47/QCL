from sys import stdin
import math
import Num_Complejos



def Sumar_vectores(vec1,vec2):
    res = []

    for i in range(len(vec1)):
        res.append(Num_Complejos.suma(vec1[i],vec2[i]))

    return res

def Inversa_vectores(vec):
    res = []

    for i in range(len(vec)):
        res.append((v[i][0]*-1, v[i][1] *-1))

    return res

def MultiplicacionEsc_vectores(con,vec):

    res = []

    for i in range (len(vec)):
        res.append(Num_Complejos.multiplicacion((con,vec[i])))

    return res

def Suma_matrices_complejas(matrix1,matrix2):
    res = []

    for i in range(len(matrix1)):
        res.append(Sumar_vectores(matrix1[i],matrix2[i]))

    return res

def inversa_matrices_complejas(matrix):

    res = []

    for i in range(len(matrix)):
        res.append(Inversa_vectores(matrix[i]))

    return res

def multiplicacionEsc_matrices_complejas(con,matrix):
    print(con)
    print(matrix)
    res = []

    for i in range(len(matrix)):
        print(matrix[i])
        res.append(MultiplicacionEsc_vectores(con,matrix[i]))
        print(res)
    return res

def Transpusta_matrices(matrix):

    res =[]

    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            pass 

def matriz_conjugada(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])

    for i in range(filas):
        for j in range(columnas):
            b = matrix[i][j]
            x = b[0]
            y = b[1]*-1
            m = (x,y)

            a[i][j] = m

    return matrix

def matriz_adjunta(matrix):
    matriz  = Transpusta_matrices(matrix)
    b = matriz_conjugada(matrix)

    return b

def norma_matrices(matrix):
    res = 0
    for i in (matrix):
        for j in i:
            res += (j[0])**2
            res += (j[1])**2

    return res ** 0.5

def matriz_distancia(matrix1,mnatrix2):
    res = 0
    for i in range (len(matrix1)):
        for j in range(len(matrix1[i])):
            val = Num_Complejos.resta(matrix[i][j],matrix2[i][j])
            res += val[0] **2 + val[1]**2
    return res ** 0.5
    


def matriz_unitaria(matrix):
    filasA = len(matrix)
    columnasA = len(matrix[0])

    if filasA == columnasA:
        res = Transpusta_matrices(matrix)
        res = matriz_conjugada(res)

        x = multiplicacionEsc_matrices_complejas(matrix,res)
        y = multiplicacionEsc_matrices_complejas(res,matrix)

        if x == y:
            return "LA MATRIZ ES UNITARIA"
        else:
            return "LA MATRIZ NO ES UNITARIA"
    else:
        print("LA MATRIZ NO ES UNITARIA")

        return False
def matriz_hermitian(matrix):
    filasA = len(matrix)
    columnasA = len(matrix[0])

    if filasA == columnasA:
        res = Transpusta_matrices(matrix)
        res = multiplicacionEsc_matrices_complejas(res)
        if res == matrix:
            return "The matrix is a hermitian matrix"
        else:
            return "The matrix A isn't a hermitian matrix"
    else:
        print("The matrix A isn't a square matrix")
        return False

def matriz_producto_tensor(matrix1,matrix2):
    filasA = len(matrix1)
    columnasA = len(matrix1[0])
    filasB = len(matrix2)
    columnasB = len(matrix2[0])

    for i in range(filasA):
        for j in range(columnasA):
            res = []
            for x in range(filasB):
                for y in range(columnasB):
                    res.append(mult(matrix1[i][j],matrix2[x][y]))
                matrix1[i][j] = res

    return matrix1
