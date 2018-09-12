sum = 0
n = int(input("Ingrese número: "))
for i in range(n):
    a = int(input(f"Número {i+1}/{n}: "))
    sum += a
print(sum)
