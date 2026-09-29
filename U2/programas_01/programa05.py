num1 = float(input("Dame un número para comparar \n:"))
num2 = float(input("Ahora un segundo número \n:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"Tanto tu primer número como el segundo son iguales.")