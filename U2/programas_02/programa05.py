(num,x)= (0,0)


while True:
    
    num = int(input("Dame un número mayor que 0 y menor que 10 \n:"))

    if (1 <= num <= 10):

        for x in range(1, num + 1):
            print(x)
        break
    else:
        print("Vuelve a introducir el número")
        