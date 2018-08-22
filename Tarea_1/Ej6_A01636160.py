#Autor: Jonathan de Jesús Chávez Tabares A01636160
nacimientos_segundo = 1/7
muertes_segundo = 1/13
tiempo = int(input("Ingrese tiempo en años: "))
tiempo *= 365*24*3600 #Paso los años a segundos

nacimientos_totales = int(nacimientos_segundo*tiempo)
muertes_totales = int(muertes_segundo*tiempo)

print("En ese tiempo nacieron {} y murieron {} personas" \
      .format(nacimientos_totales, muertes_totales))
