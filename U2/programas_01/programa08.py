import random

jugador1 = 0
jugador2 = 0

intentos = 0
for intentos in range(5): 

    #Dados del jugador 1
    dado1_j1 = random.randrange(1,7)
    dado2_j1 = random.randrange(1,7)

    #Dados del jugador 2
    dado1_j2 = random.randrange(1,7)
    dado2_j2 = random.randrange(1,7)

    sum1 = dado1_j1 + dado2_j1
    sum2 = dado1_j2 + dado2_j2

    if sum1 > sum2:
        ptos_j1 += 1
    elif sum2 > sum1:
        ptos_j2 += 1

if ptos_j1 == ptos_j2:
    if sum1 > sum2:
        