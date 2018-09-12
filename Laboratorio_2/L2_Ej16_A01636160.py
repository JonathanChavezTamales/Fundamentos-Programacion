#Autor: Jonathan Chavez A01636160
import random
rand = random.randint(1, 1000)
intentos = 7
estado = False

print(f"👴🏽 EL JUEGO DEL SIGLO 🤯\nTienes {intentos} vidas.")

while intentos > 0 and estado == False :
    guess = input("Adivina qué número pienso: ")

    if guess == "HESOYAM":
        intentos+=2
        print("+2")
    else:
        guess = int(guess)
        if guess == rand:
            print("😃 EXACTO! Ganaste. 😃")
            estado = True
        else:
            intentos -= 1
            if guess>rand:
                print("\nEs menor\t", end="")
            else:
                print("\nEs mayor\t", end="")
            for intento in range(intentos):
                print("❤️", end=" ")
            print("\n")

if estado == False:
    print("💀 GAME OVER 💀")
    print("Para ver el número que era favor de pagar en caja 1")
