#Autor: Jonathan Chávez A01636160
year = int(input("Ingrese el año: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} Año bisiesto.")

'''
Usé operadores lógicos con paréntesis
'''
