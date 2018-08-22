#Autor: Jonathan Chávez A01636160
print("FORMULA GENERAL (CHICHARRONERO)")
a = float(input("Ingrese número 'a':"))
b = float(input("Ingrese número 'b':"))
c = float(input("Ingrese número 'c':"))

if a==0:
    if b==0:
        print("Eso no es una ecuación.")
    else:
        x=-c/b
else:
    if b**2-4*a*c < 0:    #Solución imaginaria
        x1= complex( (-b + (b**2-4*a*c)**(1/2)) / (2*a) )
        x2= complex( (-b - (b**2-4*a*c)**(1/2)) / (2*a) )
        print(f"x1 = {x1:.4f} \nx2 = {x2:.4f}")
    elif b**2-4*a*c > 0:  #Numeros positivos, solución real.
        x1 =  (-b + (b**2-4*a*c)**(1/2)) / (2*a)
        x2 =  (-b - (b**2-4*a*c)**(1/2)) / (2*a)
        print(f"x1 = {x1:.4f} \nx2 = {x2:.4f}")
    else:
        print(f"Ambas raíces son iguales a: {-b/2*a}")


'''
Aprendí a usar la función complex de la librería estándar de python.
'''
