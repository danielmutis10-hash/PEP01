(num,x)= (0,0)
confirm = ""

while True:
    
    num = int(input("Dame un número mayor que 0 y menor que 10 \n:"))

    if (1 <= num <= 10):

        for x in range(1, 11):
            print(f"{num}x{x}={num*x}")

        confirm = input("Desea continuar otra vez? \n:")

        if (confirm == "Si" or confirm == "SI" or confirm == "si"):
            print("Vale :)")
        else:
            print("Finalizando programa")
            break
    else:
        print("Vuelve a introducir el número")
      