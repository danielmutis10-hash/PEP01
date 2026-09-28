
par = int(input("Dame un número que sea entero y par.\n:"))
impar = int(input("Ahora dame un número impar"))

compr_par = par % 2 == 0
compr_impar = impar % 2 != 0

if not compr_par and not compr_impar:
    print(f"tanto {par} como {impar} no son correctos")
elif not compr_par:
    print(f"{par} no es un número par")
elif not compr_impar:
    print(f"{impar} no es un número impar")
else:
    print(f"Correcto!!,{par} es par y {impar} es impar.")


