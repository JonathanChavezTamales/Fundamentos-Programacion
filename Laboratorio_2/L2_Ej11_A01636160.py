#Autor: Jonathan de Jesús Chávez Tabares A01636160
n = 0
sum = 0
i=0
mayor=0
n = int(input("Ingrese número positivo"
    " para continuar y negativo para salir:"))
while n>=0:

    sum += n
    i+=1
    n = int(input("Ingrese número positivo"
        " para continuar y negativo para salir:"))
    if n>mayor:
        mayor = n
print(f"Mayor: {mayor}  Promedio: {sum/i} Suma: {sum}")
