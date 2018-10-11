""" Funciones2 Autor: Jonathan de Jesús Chávez Tabares
    A01636160
"""
from time import sleep

VELOCIDAD_LUZ = 299792458

def energia(masa):
    """ Recibe masa y retorna energía en MKS """

    energia = masa * VELOCIDAD_LUZ**2
    return energia


def multiplos_comunes(x, y, limite):
    """ Recibe dos números y encontrará los multiplos comunes hasta límite """

    i = x*y
    comunes = []
    while(i<=limite):
        comunes.append(i)
        i*=2
    return comunes


def ofertas(monto):
    """ Recibe el monto y se aplica la promoción """

    if monto>=5 and monto<=10:
        return monto
    elif monto==25:
        return monto+3
    elif monto==50:
        return monto+8
    elif monto==100:
        return monto+20
    else:
        return 0

def barra_progreso(tiempo=3):
    """ Escribirá una X cada 10 segundos, por default 30 segundos"""
    for i in range(tiempo):
        sleep(10)
        print("X")


def menu():
    """ Despliega las opciones del menú de este programa """
    print("\n\n\n-------- Menú --------")
    print("1.-Energía\n2.-Multiplos comunes\n3.-Ofertas\n4.-Progreso\n.-Salir")
    opc = input("Ingrese número de opción")
    return opc


def main():
    opc = 1
    while(opc!="Salir"):
        opc = menu()
        if opc == "1":
            a = int(input("Ingrese masa: "))
            print(energia(a))
        elif opc == "2":
            a = int(input("Ingrese primer número: "))
            b = int(input("Ingrese segundo número: "))
            c = int(input("Ingrese límite: "))
            print(multiplos_comunes(a,b,c))
        elif opc == "3":
            a = int(input("Ingrese monto: "))
            print(ofertas(a))
        elif opc == "4":
            barra_progreso(int(input("Ingrese número de X: ")))


if __name__ == '__main__':
    main()
