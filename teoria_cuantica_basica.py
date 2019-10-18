import Matriz_Complejos
import math

def multiples_rendijas_clasico(aberturas,objetivo, probabilidad):
    posicion = 0
    respuesta = preparacion_estados_clasicos(aberturas,objetivo, probabilidad)
    
    matriz_experimental = res[0]
    probabilidad_objetivos=res[1]

    
    for i in range(1, aberturas + 1):
        matriz_experimental[i][0]= 1/(aberturas**(1/2))
        posicion = i

        
    for i in range(1, aberturas + 1):
        for j in range(posicion, posicion + probabilidad_objetivos + 1):
            matriz_experimental[j][i] = probabilidad[i-1]
    return matriz_experimental




def preparacion_estados(aberturas,objetivo, probabilidad):
    a = aberturas + 1
    b = 2 * aberturas + a * objetivo + 1
    
    probabilidad_objetivos = len(probabilidad)
    
    matriz_experimental = [[(0, 0) for j in range(b)]for i in range(b)]
    
    return (matriz_experimental,probabilidad_objetivos)




def preparacion_estados_clasicos(aberturas,objetivo, probabilidad):
    a = aberturas + 1
    b = 2 * aberturas + a * objetivo + 1
    
    probabilidad_objetivos = len(probabilidad)
    
    matriz_experimental = [[0 for j in range(b)]for i in range(b)]
    
    return (matriz_experimental,probabilidad_objetivos)



def multiples_rendijas_cuantico(aberturas,objetivo, probabilidad):
    a = aberturas + 1
    b = 2 * aberturas + a * objetivo + 1
    
    probabilidad_objetivos = len(probabilidad)
    
    matriz_experimental = probabilidad

    
    posicion = 0
    
    respuesta = preparacion_estados(aberturas,objetivo, probabilidad)
    
    matriz_experimental = res[0]
    probabilidad_objetivos = res[1]


    
    for i in range(1, aberturas + 1):
        
        matriz_experimental[i][0]= (1/(aberturas**(1/2)),0)
        
        posicion = i

        
    for i in range(1, aberturas + 1):
        for j in range(posicion, posicion + probabilidad_objetivos  + 1):
            
            matriz_experimental[j][i] =(b,0)
            
    vector=[]
    
    for i in range(b):

        if i==0:
            vector.append((1.0,0))
        else:
            vector.append((0,0))
            
    respuesta_Matrix = Matriz_Complejos.matrizmultiplication(matriz_experimental,matriz_experimental)
    respuesta = 0
    res=[]
    real=0
    imaginario = 0
    for i in range(len(vector)):
        y1=0
        y2=0
        for j in range(len(respuesta_Matrix[0])):
            
            c1=resMatrix[i][j]
            
            c2=vector[j]
            
            y1=c1[0]*c2[0]
            
            y2=c1[1]*c2[1]
            
            res.append((y1,y2))
        
    
    return res

def experimento_Canicas(matrix,estadoIni,numCambios):
    for i in range(numCambios):
        
        estadoIni = cambios(matrix,estadoIni)

        
    return estadoIni


def cambios(matrix,estadoini):
    
    res=0
    
    vector=[]
    for i in range(len(estadoini)):
        for j in range(len(estadoini)):
            
            res+=matrix[i][j]*estadoini[j]

        vector.append(res)
        res=0
        
    return vector
