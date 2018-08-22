#Autor: Jonathan Chávez A01636160
PI = 3.14159
radio_menor = float(input("Ingrese radio menor: "))
radio_mayor = float(input("Ingrese radio mayor: "))
altura = float(input("Ingrese altura: "))

if radio_menor<0 and radio_mayor<0 and altura<0:
    print("Datos incorrectos, verifica.")
else:
    volumen = PI*altura*( radio_mayor**2 + radio_menor**2 + \
              radio_mayor*radio_menor ) / 3
    print("Volumen de tronco de cono: {:.2f}".format(volumen))

 '''
 Aprendí a hacer expresiones multilinea con \
 '''
