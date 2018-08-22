#Autor: Jonathan de Jesús Chávez Tabares A01636160
segundos = int(input("Ingrese la hora en segundos: "))
horas = segundos//3600
minutos = segundos%3600//60
segundos = segundos%3600%60

print(str(horas) + " horas, " + str(minutos) + " minutos y " + \
      str(segundos) + " segundos.")

'''
Algunas funciones me quedaron largas
tuve que cortarlas y no sé cómo iba la identación
https://doingmathwithpython.github.io/breaking-long-lines-in-python.html
'''
