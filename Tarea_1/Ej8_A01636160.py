#Autor: Jonathan de Jesús Chávez Tabares A01636160
print("Calculadora de resistencias en paralelo (Ohmios)")
r1 = float(input("Escriba resistencia 1"))
r2 = float(input("Escriba resistencia 2"))
r3 = float(input("Escriba resistencia 3"))

rt = 1 /(1/r1 + 1/r2 + 1/r3) #Formula de total de resistencias en paralelo

print("La resistencia total es: {:.8f} Ohmios".format(rt))


'''
Ya escribo python bien chido
'''
