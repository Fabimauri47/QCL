def ProductoInterno(v1, v2):
    if len(v1) == len(v2):
        cont = (0, 0)
        for i in range(len(v1)):
            m = mult(v1[i], v2[i])
            n = (cont[0]+m[0], cont[1]+m[1])
            cont = n
        return cont
    else:
        return False


def amplitud(n1, n2, k1, k2):
    k3 = k2
    r1 = innerproduct(n1, k1)
    r2 = innerproduct(n2, k2)
    return innerproduct(r1, r2)


def probabilidad(h, ket):
    r = normofcomplexvector(ket)
    x = ket[h]
    y = x
    sum_1 = mult(x, y)
    sum_2 = abs(sum_1[0] + sum_1[1])
    pro = sum_2/(r ** 2)
    return pro


def varianca(M, v):
    if len(M) == len(v[0]):
        H = matrizmultiplication(M, transpose(v))
        w = [[]]
        for j in H:
            w[0].append(j[0])
        x = matrizmultiplication(transpose(w), v)
        E = x[0][0][0] + x[1][0][1]
        m1 = ident(E, M)
        N = resta(M, m1)
        Delta = matrizmultiplication(N, N)
        r = v
        for i in range(len(v)):
            for j in range(len(v[0])):
                x = v[i][j]
                c = x[0] ** 2
                t = x[1] ** 2
                r[i][j] = (c, t)
        Rf = matrizmultiplication(r, Delta)
        x = prube(Rf[0][0])
        return round(x[0], 1)
    else:
        return False


def estadosCompuertas(ob, v):
    ob1 = []
    for i in range(len(ob)):
        ob1.append([])
        for j in range(len(ob[0])):
            ob1[i].append(ob[i][j])
    for i in range(len(ob1)):
        for j in range(len(ob1[0])):
            ob1[i][j] = egval(ob1[i][j])
    N = list(LA.eig(ob1)[0])
    y = variance(ob, v)
    return N, y
