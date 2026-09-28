par = int(input("Dame un número que sea par, no importa si es positivo o negativo\n:"))

compr_par = par % 2 == 0

if not compr_par:
    print(f"{par} no es par")
else:
    impar = int(input("Ahora dame un número impar, no importa que sea negativo\n:"))

    compr_impar = impar % 2 != 0 

    if not compr_impar:
        print(f"{impar} no es un número impar")
    else:
        print("Ambos números son correctos.")