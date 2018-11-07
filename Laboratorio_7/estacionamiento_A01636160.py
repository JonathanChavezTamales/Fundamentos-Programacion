import random

def simulacion():
    file = open('lugares.txt', 'w+')
    for i in range(10):
        for j in range(15):
            file.write(str(random.randint(0,1))+',')
        file.write('\n')
    file.close()


def lee_archivo(file):
    file = open(file, 'r')
    matriz = []
    for line in file:
        matriz.append(line.rstrip().split(','))
    r = []
    for i in matriz:
        i.pop()
        r.append(list(map(lambda x:int(x), i)))
    return r

def cuenta_vacios(disponibilidad):

    """ Retorna lugares vacíos de un estacionamiento """



    letras = ['a','b','c','d','e','f','g','h','i','j']

    vacios = []

    for i in range(len(disponibilidad)):
        for j in range(len(disponibilidad[i])):
            if disponibilidad[i][j] == 0:
                vacios.append(letras[i]+str(j))

    return vacios



def main():
    print("Recolectando datos...")
    simulacion()
    print("Leyendo...")
    matriz = lee_archivo("lugares.txt")
    print("\n\n\nLos lugares vacíos son:")
    print(cuenta_vacios(matriz))


main()
