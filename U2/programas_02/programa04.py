num_secreto = 45
num = 0

while (num != num_secreto):
    num = int(input("Introduce el número secreto \n:"))

if (num==num_secreto):
    print("¡Has dejado el bucle con éxito")

#Primera versión

while True:
    num = int(input("Introduce el número secreto:\n"))
    if num == num_secreto:
        print("¡Has dejado el bucle con éxito!")
        break