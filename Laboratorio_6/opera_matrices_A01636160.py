def suma_matrices(m1,m2):
    suma = [[] for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            suma[i].append(m1[i][j] + m2[i][j])
    return suma

def resta_matrices(m1,m2):
    resta = [[] for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            resta[i].append(m1[i][j] - m2[i][j])
    return resta

def escalar(m1,n):
    s = [[] for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            s[i].append(m1[i][j] * n)
    return s

def multiplica_matrices(m1,m2):
    s = [[] for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            c = 0
            for k in range(len(m2)):
                c += m1[i][k]*m2[k][j]
            s[i].append(c)
    return s

def traspuesta(matriz):
    traspuesta = [[] for j in matriz[0]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            traspuesta[j].append(matriz[i][j])
    return traspuesta

def triangular(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i>j and matriz[i][j]!=0:
                return False
    return True

a = [[3, 7, 5],
     [12,2,11]]

b = [[3,16],
     [1,4],
     [4,22]]

print(multiplica_matrices(a,b))
