import random

print("1. Piedra\n")
print("2. Papel\n")
print("3. Tijera\n")
print("\n")
usuario = int(input("Seleccione una opción (1, 2 o 3) \n: "))

# Validar que la opción elegida sea correcta
if usuario not in [1, 2, 3]:
    print("Error: Opción no válida. Debes introducir 1, 2 o 3.")
else:
    # Elección aleatoria del ordenador
    ordenador = random.randint(1, 3)

    # Nombres de las opciones para mostrar por pantalla
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

    print(f"\nTu elección: {opciones[usuario]}")
    print(f"Elección del ordenador: {opciones[ordenador]}\n")

    # Determinación del resultado
    if usuario == ordenador:
        print("¡Ha sido un empate!")
    elif (usuario == 1 and ordenador == 3) or (usuario == 2 and ordenador == 1) or (usuario == 3 and ordenador == 2):
        print("¡Has ganado!")
    else:
        print("¡Ha ganado el ordenador!")