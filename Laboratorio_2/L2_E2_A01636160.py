#Autor: Jonathan de Jesús Chávez Tabares A01636160
#Secuencia de Siracusa (Collatz/Hailstone)
n = int(input("Ingrese número para calcular la secuencia Siracusa: "))
print(n)
while n!=1:
    if n%2 == 0:
        n/=2
    else:
        n = 3*n+1
    print(int(n), end=",")


'''
Usé condicional dentro de while
aprendí a usar end= en print para quitar el default de \n
'''
