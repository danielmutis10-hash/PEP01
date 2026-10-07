import random

ordenador = random.randrange(17,22)
cont = 0

while True:

    print(f"Puntuación actual: {cont}")
    opc = input("Tomas una carta? \n:")

    if (opc == "SI" or opc == "si" or opc == "Si"):

        cartas_jugador = random.randrange(1,6)
        cont += cartas_jugador

        if (cont > 21):
            print(f"Jugador pierde por sobrepasar 21 \nPuntuación jugador: {cont}")
            break

    elif (opc == "No" or opc == "NO" or opc == "no"):

        if (ordenador < cont < 21):
            print(f"Jugador gana \nPuntuación jugador: {cont} \nPuntuación banca: {ordenador}")
            break
        else:
            print(f"Jugador pierde \nPuntuación jugador: {cont} \nPuntuación banca: {ordenador}")
            break
    
    
