num1 = int(input("Dame un número\n:"))
num2 = int(input("Ahora un sefundo número\n:"))

if num2 == 0:
    print("No se puede dividir por cero")
else:
    resultado = num1 / num2

    print(f"{resultado} es el resultado de la operación")