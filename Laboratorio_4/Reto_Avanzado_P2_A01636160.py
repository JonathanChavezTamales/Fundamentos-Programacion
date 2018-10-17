""" Juego del ahorcado """


from time import sleep
from random import randrange

palabras = ["gato", "perro", "elefante", "mariposa", "leon", "rana",
            "pez", "borrego", "canguro", "ballena", "delfin"]

class Player:
    def __init__(self, name, vidas, puntos):
        self.name = name
        self.vidas = vidas
        self.puntos = puntos


def show_title(player):


    title = "   💀💀 🅰 🅷 🅾 🆁 🅲 🅰 🅳 🅾 💀💀"
    print(50*"*")
    sleep(.3)
    print("\t",title)
    sleep(.3)
    print(50*"*")
    sleep(.3)
    print(f"\n\tBienvenid@, {player.name}")
    print("\n\t\t1.-Nuevo Juego\n\t\t2.-Registro\n\t\t3.-Leaderboard"\
         +"\n\t\t4.-Salir")


def new_game(player):
    """Aquí se puede usar random.choice(lista) y se puede optimizar con lista
    anidada """

    #Se inicializan las vidas
    player.vidas = 6

    #Se escoge la palabra y sus caracteres no son adivinados
    palabra = palabras[randrange(0,len(palabras))]
    estado_palabra = [x*0 for x in range(len(palabra))]

    print("\n\n\t\tI N S T R U C C I O N E S")
    print(">>>Solo escriba la palabra o la letra que crea correcta \n"\
         +">>>Escriba únicamente en minúsculas y sin tildes.")
    print("\t\t\t", end="")

    #Bandera para saber si ganó (1), perdió (-1) o todavía no acaba (0)
    win_status = 0
    while win_status == 0:
        i = 0
        print(f"\n{player.name}\t\t\t\tVidas: "+ player.vidas*"❤️ ")
        draw(player.vidas)

        print("\t\t\t", end="")

        #Imprime los espacios blancos o las letras
        while i<len(palabra):
            if estado_palabra[i] == 0:
                print("_ ", end="")
            else:
                print(palabra[i]+" ", end="")

            i+=1

        guess = input("\n\nIngrese una sola letra o la palabra: ")


        """Lógica de comparación de palabras """


        if guess == palabra:
            print("HAS GANADO! La palabra fue ",palabra)
            win_status = 1
            player.puntos += 1

        elif len(guess)>1:
            print("\n¡Solamente ingrese una letra o una palabra!")

        elif guess in palabra:

            #Cambia el estado de cada caracter que coincida con el leído
            for i, j in enumerate(palabra):
                if j == guess:
                    estado_palabra[i] = 1

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
            player.puntos += 1




def register(player):
    print(f"¿No eres {player.name}?\nInicia sesión ahora.")
    name = input("Ingresa tu usuario:  ")
    global current_player = Player(name, 6, 0)
    print(current_player.name)
    print(player.name)
    input("Toque enter para salir.")


def leaderboard(player):
    print(f"\n\n\nTu puntaje: {player.puntos}")
    input("Toque enter para salir.")

def draw(vidas):

    if vidas == 6:
        print("__________\n|       |\n|\n|\n|\n|\n|\n|\n|\n--")
    elif vidas == 5:
        print("__________\n|       |\n|      😵\n|\n|\n|\n|\n|\n|\n--")
    elif vidas == 4:
        print("__________\n|       |\n|      😵\n|      / \n|"\
        +"\n|\n|\n|\n|\n--")
    elif vidas == 3:
        print("__________\n|       |\n|      😵\n|      / \\\n|"\
        +"\n|\n|\n|\n|\n--")
    elif vidas == 2:
        print("__________\n|       |\n|      😵\n|      / \\\n|"\
        +"\t|\n|\n|\n|\n|\n--")
    elif vidas == 1:
        print("__________\n|       |\n|      😵\n|      / \\\n|"\
        +"\t|\n|      /\n|\n|\n|\n--")
    elif vidas == 0:
        print("__________\n|       |\n|      😵\n|      / \\\n|"\
        +"\t|\n|      /\\\n|\n|\n|\n--")

def main():

    game_status = True
    current_player = Player("Invitado", 6, 0)

    while game_status==True:

        show_title(current_player)
        opc = input("\nIngrese una opción: ")

        if opc == "1":
            new_game(current_player)
        elif opc == "2":
            register(current_player)
        elif opc == "3":
            leaderboard(current_player)
        elif opc == "4":
            game_status = False
    print("Jonathan Chávez")

if __name__ == '__main__':
    main()
