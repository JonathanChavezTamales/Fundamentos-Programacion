palabra = input("Ingrese cadena")
sum = 0
lis = "AEIOUaeiou"
for car in palabra:
    if car in lis:
        sum+=1
print(sum)
