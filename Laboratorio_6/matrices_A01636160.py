""" Ejercicios de listas anidadas """


def creaMatriz1(n):
    """Crea matriz  con elementos -1"""

    return [[-1 for i in range(n)] for i in range(n)]


def creaMatriz2(n):
    """Crea matriz  donde cada elemento tiene su # de columna como valor"""

    return [[i for i in range(n)] for i in range(n)]


def creaMatriz3(n):
    """Crea matriz  donde cada elemento tiene su # de fila como valor"""

    return [[j for i in range(n)] for j in range(n)]


def creaMatriz4(n):
    """Crea matriz  donde los elementos van consecutivos en vertical"""
    lista = []
    x = 1
    for i in range(n):
        sublista = []
        for j in range(n):
            sublista.append(j*n+x)
        lista.append(sublista)
        x += 1
    return lista


def cuentaPares(lista):
    """Cuenta el # de pares en la matriz """

    count = 0
    for i in lista:
        for j in i:
            if j%2==0:
                count += 1

    return count


def sumaMatriz(lista):
    """ Suma de todos los elementos de la matriz """


    suma = 0
    for i in lista:
        suma += sum(i)
    return suma


def cuentaPositivos(lista):
    """ Cuenta el # de positivos en una matriz  """

    c = 0
    for i in lista:
        for j in i:
            if i>0:
                c+=1
    return c


def cambiaNegativos(lista):
    """ Cambia los negativos por 0 en una matriz """

    for i in lista:
        for j in range(len(i)):
            if i[j]<0:
                i[j]*=0
    return lista


def cuentaRepeticiones(lista,a):
    """ Cuenta cuántas veces se repite un número en una matriz """

    c = 0
    for i in lista:
        for j in lista:
            if j == a:
                c+=1
    return c


def busca(lista, x):
    """ True si un elemento se encuentra en la matriz"""

    for i in lista:
        if x in i:
            return True
    return False


def sumaMayores5(lista):
    """ Suma de los elementos mayores a 5 en una matriz """

    suma = 0
    for i in lista:
        for j in i:
            if j>5:
                suma += j
    return suma


def cambiaCeros(lista):
    """ Cambia los 0 en una matriz por el producto de sus coordenadas"""

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i][j]==0:
                lista[i][j]=i*j
    return lista



def _printMatrix(matrix):
    """ Aux: Imprime una matriz bidimensional """

    for i in matrix:
        for j in i:
            print(f"{j} | ", end="")
        print("\n")
