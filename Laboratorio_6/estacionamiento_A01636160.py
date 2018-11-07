""" Retorna lugares vacíos de un estacionamiento """

disponibilidad = [
            [1,0,0,1,1,0,1,1,1,0],
            [0,0,0,0,1,0,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],
            [0,0,0,0,1,0,1,1,1,1],

          ]

letras = ['a','b','c','d','e','f','g','h','i','j']

vacios = []

for i in range(len(disponibilidad)):
    for j in range(len(disponibilidad[i])):
        if disponibilidad[i][j] == 0:
            vacios.append(letras[i]+str(j))

print(vacios)
