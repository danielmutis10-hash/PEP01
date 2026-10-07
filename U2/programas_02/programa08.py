import random

num_secreto = random.randrange(1,21)

while (num != num_secreto):
    num = int(input("Dame un nçumero para ver si es el nçumero secreto entre 1 y 20"))

    if (num > num_secreto):
        print("El número es menor")
    elif (num < num_secreto):
        print("El número es mayor")
    elif (num == num_secreto):
        print("Correcto")
    else:
        print("número incorrecto")

while (num != num_secreto or intentos == 3):
    num = int(input("Dame un nçumero para ver si es el nçumero secreto entre 1 y 20"))

    if (num > num_secreto):
        print("El número es menor")
        intentos += 1
    elif (num < num_secreto):
        print("El número es mayor")
        intentos += 1
    elif (num == num_secreto):
        print("Correcto")
    else:
        print("número incorrecto")

    if(intentos == 3):
        print("Número de intentos acabados")
