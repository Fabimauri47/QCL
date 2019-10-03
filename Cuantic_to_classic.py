import Matriz_Complejos

def marbles(matrix, vec, push):

    if len(matrix) == len(vec):

        res = vec
        while push != 0:
            
            res = Matriz_Complejos.Accion_Matriz_Vector(matrix,res)
            push -= 1

        return res

    else:
        print("Incorrect dimensions. Please retype.")

def Probability(matrix, vec):

    res= vec
    
    if len(matrix) == len(vec):        
        res = Matriz_Complejos.Accion_Matriz_Vector(matrix,res)
        return res
    else:
        print("Incorrect dimensions. Please retype.")

def DoubleSlit(matrix):

    res = MultiplicacionEsc_matrix(matrix,matrix)
    return res
