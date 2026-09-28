num = float(input("Dame la nota"))

if num >= 0 and num <5:
    print("Insuficiente")
elif num >=5 and num <6:
    print("Suficiente")
elif num >=6 and num <7:
    print("Bien")
elif num >=7 and num <9:
    print("Notable")
elif num >= 9 and num <=10:
    print("Sobresaliente")
else:
    print("Número incorrecto")