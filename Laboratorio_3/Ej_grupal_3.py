pares = 0
impares = 0
for n in range(10):
    a = int(input(f"Número {n+1}/10: "))
    if a%2 == 0:
        pares+=1
    else:
        impares+=1
print(f"Pares: {pares}\nImpares: {impares}")


pares = 0
impares = 0

n_max = int(input("Ingrese cantidad de números a escribir: "))
for n in range(n_max):
    a = int(input(f"Número {n+1}/{n_max}: "))
    if a%2 == 0:
        pares+=1
    else:
        impares+=1
print(f"Pares: {pares}\nImpares: {impares}")
