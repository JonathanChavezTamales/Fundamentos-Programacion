#Autor: Jonathan de Jesús Chávez Tabares A01636160
from math import sqrt

lado_a = float(input("Ingrese lado A: "))
lado_b = float(input("Ingrese lado B: "))
lado_c = float(input("Ingrese lado C: "))

#FORMULA DE HERON
sp = (lado_a+lado_b+lado_c)/2 #semiperimetro
area = sqrt(sp*(sp-lado_a)*(sp-lado_b)*(sp-lado_c))

print(f"El área del triángulo es: {area:.2f}") #mostrar con 2 decimales

'''
Aprendí a importar y a utilizar la palabra from
y descubrí que math es un módulo que ya viene en la librería
estándar y por eso no se descarga.

Los módulos son códigos .py que pueden ser insertados en nuestro
código, algo así como los headers en C++.

Un módulo es un refrigerador que tiene varias frutas (funciones) dentro
Al hacer 'import math' estoy metiendo el refrigerador, y tengo que abrir
el refrigerador para sacar la fruta.

Si hago 'from math import *' es como si sacara la fruta y ya no tengo que
abrir el refri. El problema es cuando hay más de un refrigerador
y la frutas similares.

https://stackoverflow.com/questions/30646650/from-math-import-sqrt- 
works-but-import-math-does-not-work-what-is-the-reaso

https://discuss.codecademy.com/t/import-math-vs-from-math-
import-is-there-a-difference/43314/2
'''
