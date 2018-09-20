n = int(input("Ingrese n: "))

if n>0:
    sum = 0

    #Método 2 O(n)
    for i in range(1, n+1):
        if i%2 == 0:
            sum += i
        else:
            sum -= i
    print(sum)

    #Método 2 sin ciclo O(2)
    if n%2 == 0:
        sum = n//2
    else:
        sum = (n//2) * -1

    print(sum)

else:
    print("valor no válido")
