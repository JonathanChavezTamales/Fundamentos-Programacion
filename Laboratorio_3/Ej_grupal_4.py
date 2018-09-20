n = int(input("Ingrese n: "))

if n>0:
    #Método 1

    print(sum(list(range(1,n+1))))

    #Método 2 Ciclo
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)

    #Método 3 Matemático
    print(int(n*(n+1)/2))

else:
    print("Número no valido")
