def perimetro(*p):
	"""Calcula a distancia entre n puntos y la suma"""
	""" Atributos:
		-p: puntos indefinidos, deben de ir secuenciados x y y
	"""

	if len(p)%4 != 0:
		return 1

	i = 0
	sum = 0
	while i<len(p):
		sum += ((p[i+1]-p[i])**2 + (p[i+3]-p[i+2])**2)**(1/2)
		i += 4

	return sum

print(perimetro(1,2,3,4,9,8,7,6))
