year = int(input("Introduce el año: "))

leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 )

if not leap_year:
    print(f"El año no es bisiesto")
else:
    print(f"El año es bisiesto")
