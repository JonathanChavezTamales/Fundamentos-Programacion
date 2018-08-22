#Autor: Jonathan de Jesús Chávez Tabares A01636160
dinero_actual = float(input("Ingrese su dinero actual: "))
tasa_interes = float(input("Ingrese su tasa de interés (%): "))
tiempo_interes = int(input("Ingrese su tiempo en años: "))
rendimiento = dinero_actual*tasa_interes*tiempo_interes/100

print(f"""Su rendimiento al final de {tiempo_interes} años
es de {rendimiento}""")

'''
Aquí aprendí a usar el formateo con la f, es recomendado para usar
con python 3.x
https://realpython.com/python-f-strings/
'''
