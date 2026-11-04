num = 0
while True:
    try:
        num = int(input("Introduce un valor entre 1 y 10: "))

        if 1 <= num <= 10:
            print(f"Correctom introduciste el número {num}")
            break
        else:
            print("El número debe estár entre 1 y 10. Intentalo otra vez.\n")

    except ValueError:
        print("Error: debes introducir obligatoriamente un número entero válido.\n")