cadena1 = input("Cadena 1: ")
cadena2 = input("Cadena 2: ")
comun = []
for i in cadena1:
    if i in cadena2:
        if i not in comun:
            comun.append(i)

print(comun)

# Aprendí a usar una función built-in: .append
