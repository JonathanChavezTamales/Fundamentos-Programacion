#Autor: Jonathan de Jesús Chávez Tabares A01636160
from random import randrange
minimo = int(input("Ingrese mínimo: "))
maximo = int(input("Ingrese máximo: "))
print("VOY A ADIVINAR EL NÚMERO QUE PIENSAS")
estado = ""

while estado!="igual":
    guess = int((minimo+maximo)/2)
    print(f"Es {guess} ?: ", end="")
    estado = input()
    if estado=="mayor":
        minimo = guess
    elif estado=="menor":
        maximo = guess
print("HE ADIVINADO")


'''
Hecho con búsqueda binaria
'''
