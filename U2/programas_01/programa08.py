import random

# Tirada de dados del Jugador 1
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
sum1 = dado1_j1 + dado2_j1
max_j1 = max(dado1_j1, dado2_j1)

# Tirada de dados del Jugador 2
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
sum2 = dado1_j2 + dado2_j2
max_j2 = max(dado1_j2, dado2_j2)

# Mostrar tiradas en pantalla
print(f"Jugador 1: dados [{dado1_j1}, {dado2_j1}], suma: {sum1}")
print(f"Jugador 2: dados [{dado1_j2}, {dado2_j2}], suma: {sum2}")

# Evaluacion de las condiciones del juego
if sum1 > sum2:
    print(f"Gana el Jugador 1 ({sum1} vs {sum2}).")
elif sum2 > sum1:
    print(f"Gana el Jugador 2 ({sum2} vs {sum1}).")
else:
    # Empate en puntuación total
    print("¡Empate en suma total! Comprobando el dado más alto...")
    if max_j1 > max_j2:
        print(f"Gana el Jugador 1 al tener el dado más alto ({max_j1} vs {max_j2}).")
    elif max_j2 > max_j1:
        print(f"Gana el Jugador 2 al tener el dado más alto ({max_j2} vs {max_j1}).")
    else:
        print(f"¡Han empatado completamente! Ambos tienen el dado más alto en {max_j1}.")