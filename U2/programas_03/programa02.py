num = 0
i = 0
while True:
    try:
        num = int(input("Introduce un número entre 1 y 10 para ver la lista: "))

        if 1 <= num <= 10:
            print(f"Mostrando los números del 1 al {num}:")
            for i in range(1, num + 1):
                print(i)
            break
        else:
            print("El número no puede ser menor que 1 ni mayor que 10.\n")
            
    except ValueError:
        print("Error: Entrada no válida. Introduce un número entero.\n")