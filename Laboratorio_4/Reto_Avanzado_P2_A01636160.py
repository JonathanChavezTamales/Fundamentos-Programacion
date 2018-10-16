""" Juego del ahorcado """


from time import sleep
from random import randrange

palabras = ["gatoo"]

class Player:
    def __init__(self, name, vidas, puntos):
        self.name = name
        self.vidas = vidas
        self.puntos = puntos


def show_title():


    title = "   💀💀 🅰 🅷 🅾 🆁 🅲 🅰 🅳 🅾 💀💀"
    print(50*"*")
    sleep(.3)
    print("\t",title)
    sleep(.3)
    print(50*"*")
    sleep(.3)
    print("\n\t\t1.-Nuevo Juego\n\t\t2.-Registrarse\n\t\t3.-Iniciar sesión"\
         +"\n\t\t4.-Salir")


def new_game(player):
    """Aquí se puede usar random.choice(lista) y se puede optimizar con lista
    anidada """


    palabra = palabras[randrange(0,len(palabras))]
    estado_palabra = [x*0 for x in range(len(palabra))]
    print("\t\t\t", end="")

    #Bandera para saber si ganó (1), perdió (-1) o todavía no acaba (0)
    win_status = 0
    while win_status == 0:
        i = 0
        print(f"\n{player.name}\t\t\t\tVidas: "+ player.vidas*"❤️ ")
        draw()

        print("\t\t\t", end="")
        while i<len(palabra):
            if estado_palabra[i] == 0:
                print("_ ", end="")
            else:
                print(palabra[i]+" ", end="")

            i+=1

        guess = input("\n\nIngrese una letra o palabra: ")


        """Lógica de comparación de palabras """


        if guess == palabra:
            print("HAS GANADO! La palabra fue ",palabra)
            win_status = 1

        elif guess in palabra:
            for i, j in enumerate(palabra):
                if j == guess:
                    print("q rollo")
                    estado_palabra[i] = 1

        elif guess == palabra:
            print("HAS GANADO! La palabra fue",palabra)
            win_status = 1

        else:
            player.vidas -= 1


        #Revisa si ha perdido
        if player.vidas <= 0:
            print("HAS PERDIDO! La palabra fue",palabra)
            win_status = -1

        #Revisa si ha ganado
        if sum(estado_palabra)==len(estado_palabra):
            print("HAS GANADO! La palabra fue",palabra)
            win_status = 1



def register(player):
    print("¡Regístrate ahora!")
    input("Toque enter para salir.")


def login(player):
    print(f"¿No eres {player.name}?\nInicia sesión ahora.")
    input("Toque enter para salir.")

def draw():
    print("__________\n|       |\n|\n|\n|\n|\n|\n|\n|\n--")


def main():

    game_status = True
    current_player = Player("Invitado", 3, 0)
    while game_status==True:

        show_title()
        opc = input("\nIngrese una opción: ")

        if opc == "1":
            new_game(current_player)
        elif opc == "2":
            register()
        elif opc == "3":
            login(current_player)
        elif opc == "4":
            game_status = False
    print("Jonathan Chávez")

if __name__ == '__main__':
    main()
