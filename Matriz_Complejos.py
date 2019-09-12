import Num_Complejos



def Sumar_vectores(vec1,vec2):
    res = []

    for i in range(len(vec1)):
        res.append(Num_Complejos.suma(vec1[i],vec2[i]))

    return res

def Inversa_vectores(vec):
    res = []

    for i in range(len(vec)):
        res.append((vec[i][0]*-1, vec[i][1] *-1))

    return res

def MultiplicacionEsc_matrix(con,vec):

    res = []
    #print(vec)

    for i in range (len(vec)):
        fila = []
        for j in range(len(vec[i])):
            fila.append(Num_Complejos.multiplicacion(con,vec[i][j]))
        res.append(fila)
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

def multiplicacionEsc_vector_complejas(con,matrix):
   
    res = []

    for i in range(len(matrix)):
        res.append(Num_Complejos.multiplicacion(con,matrix[i]))
    
    return res

def Transpusta_matrices(matrix):

    res =[]

    for i in range(len(matrix[0])):
        fila = []
        for x in range(len(matrix)):
            fila.append(matrix[x][i])
        res.append(fila)
    return res

def matriz_conjugada(matrix):
    res = []

    for i in range(len(matrix)):
        Conjugado = []
        for j in range(len(matrix[i])):
            Conjugado.append(Num_Complejos.conjugado(matrix[i][j]))
        res.append(Conjugado)

    return res

def matriz_adjunta(matrix):
    matriz  = Transpusta_matrices(matrix)
    matriz = matriz_conjugada(matriz)

    return matriz

def norma_matrices(matrix):
    res = 0
    for i in (matrix):
        for j in i:
            res += (j[0])**2
            res += (j[1])**2

    return res ** 0.5

def matriz_distancia(matrix1,matrix2):
    res = 0
    for i in range (len(matrix1)):
        for j in range(len(matrix1[i])):
            val = Num_Complejos.resta(matrix1[i][j],matrix2[i][j])
            res += val[0] **2 + val[1]**2
    return res ** 0.5

def matrizmultiplication(matriz1, matriz2):
    
    filasMatriz2 = len(matriz2)
    columnasMatriz1 = len(matriz1[0])
    
    if filasMatriz2 == columnasMatriz1:
        filas = len(matriz1)
        columnas = len(matriz2[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(matriz2)):
                    m = Num_Complejos.multiplicacion(matriz1[i][k], matriz2[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])

    
def MatrizIdentidad(fila,columna):

    identidad = [[(0,0)]*fila for i in range(columna)]

    for i in range(fila):
        for j in range(columna):

            if i==j:
                identidad[i][j] = (1,0)

def RevisarUnitaria(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    if filas == columnas:
        transpuesta = Transpusta_matrices(matriz)
        matriz = matrizmultiplication(matriz,transpuesta)
        identidad = MatrizIdentidad(filas,columnas)

        if matriz == identidad:
            return True
        
        else:
            return False

        return False
def MatrizHermitania(matriz):

    if matriz == matriz_adjunta(matriz):
        return True
    else: return False

    
def Accion_Matriz_Vector(matrix,vector):

    res = []

    if len(matrix[0]) == len(vector):
        Suma = (0,0)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp = Num_Complejos.multiplicacion(matrix[i][j],vector[j])
                Suma = Num_Complejos.suma(temp,Suma)

            res.append(Suma)
            Suma = (0,0)
        return res
    else:

        return "Dimensiones incorrectas"
    
                
def ProductoTensor(dato1,dato2):

    respuesta = []
    control = 0
    posicioni = 0
    posicionj = 0

    while (posicioni < (len(dato1)-1)*2):
        fila1 = dato1[posicioni]
        fila2 = dato2[posicionj]
        fila = []
        
        for i in fila1:
            for j in fila2:
                fila.append(Num_Complejos.multiplicacion(i,j))
        
        posicionj += 1
        fila2 = dato2[posicionj]
        respuesta.append(fila)
        fila = []
        
        for i in fila1:
            for j in fila2:
                fila.append(Num_Complejos.multiplicacion(i,j))
                
        posicioni += 1
        posicionj -= 1
        respuesta.append(fila)
   
    return respuesta
