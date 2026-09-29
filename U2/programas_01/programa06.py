day = int(input("Introduce el día: "))
month = int(input("Introduce el mes: "))
year = int(input("Introduce el año: "))

if year <= 0 or month < 1 or month > 12:
    confirm = False
else:

    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 )

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            max_day = 31
        case 4 | 6 | 9 | 11 :
            max_day = 30
        case 2:
            if leap_year:

                max_day = 29

            else: 

                max_day = 28

    confirm = 1 <= day <= max_day

if confirm:
    print(f"La fecha {day}/{month}/{year} es correcta")
else: 
    print(f"La fecha {day}/{month}/{year} es incorrecta")
