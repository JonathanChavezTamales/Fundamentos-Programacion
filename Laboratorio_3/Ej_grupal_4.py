n = int(input("Ingrese n: "))


#Método 1
print(sum(list(range(1,n+1))))

#Método 2
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#Método 3
print(int(n*(n+1)/2))
