#Autor: Jonathan Chavez A01636160
n = int(input("Ingrese número para calcular factorial: "))
i = 1
fact = 1
while i<=n:
    fact = i*fact
    i += 1

print("El factorial es ",fact)
