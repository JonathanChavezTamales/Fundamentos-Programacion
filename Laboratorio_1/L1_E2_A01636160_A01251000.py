#Santiago Yeomans
#A01251000

print("Ingresa 3 numeros que quieras")

a = float(input("Escribe el primer numero: "))
b = float(input("Escribe el segundo numero: "))
c = float(input("Escribe el tercer numero: "))

if a == b and b == c:
    print("\nLos 3 numeros son iguales")
    
elif a == b or b == c or a == c:
    print ("\n2 de tus numeros son iguales")
    
else:
    print ("\nTodos tus numeros son diferentes")

#Con esta actividad aprendi a utilizar los comparadores logicos and y or
