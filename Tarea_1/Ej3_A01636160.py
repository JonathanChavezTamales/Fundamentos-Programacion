#Autor: Jonathan de Jesús Chávez Tabares A01636160
peso_libras = float(input("Escriba su peso en libras: "))
altura_pulgadas = float(input("Escriba su altura en pulgadas: "))
peso = peso_libras/2.2046
altura = altura_pulgadas*0.0254
imc = peso/altura**2
print("Su IMC es %s" % (imc))

'''
Aprendí formateos de strings más avanzados y que el método format es más nuevo
Fuente: https://pyformat.info/
'''
