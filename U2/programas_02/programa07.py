(num,suma,aux) = (0,0,0)
media = 0.0
print("Dame números para sumar y realizar la media, hasta que pongas 0 y termine el programa")
num = int(input(":"))
while (num != 0):
    num = int(input(":"))
    aux += 1
    suma += num

media = float(suma/aux)

print(f"Suma: {suma}")
print(f"Media: {media}")


print("Dame números para sumar y realizar la media, hasta que pongas 0 y termine el programa")
num = int(input(":"))
while True:
    num = int(input(":"))
    aux += 1
    suma += num
    if (num == 0):
        break

media = float(suma/aux)

print(f"Suma: {suma}")
print(f"Media: {media}")