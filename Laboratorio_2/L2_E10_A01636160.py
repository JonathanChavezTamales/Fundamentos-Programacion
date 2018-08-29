#Autor: Jonathan de Jesús Chávez Tabares A01636160
#Verificar si es número perfecto, si la suma de sus divisores da el mismo número
n = int(input("Ingrese número para verificar si es perfecto: "))
cont = 1 #Índice del divisor
aum = 0; #Suma de los divisores
while cont<n:
    if n%cont == 0: #Si es divisor
        aum+=cont   #Sumarlo a la cuenta
    cont+=1
if aum == n:
    print(f"{n} es perfecto.")
else:
    print(f"{n} no es perfecto.")


'''
Usé aumento y contador
'''
