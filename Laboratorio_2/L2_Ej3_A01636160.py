#Autor: Jonathan de Jesús Chávez Tabares A01636160
capital = float(input("Ingrese el capital inicial: "))
interes = float(input("Ingrese el interés anual (%): "))
time = 0
capital_final = 2*capital
while capital<capital_final:
    capital += capital*interes/100
    time+=1

print("Se duplicará pasando ", time ," año/s")


'''
Puede pasarse el capital del capital capital_final
Para hacerlo exacto es mejor despejar el tiempo de la formula del interes
compuesto
'''
