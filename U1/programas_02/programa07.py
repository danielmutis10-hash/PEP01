minutes_input = input("Dime cuantos minutos quieres poner para decirte cuantas horas son. \n:")

try:
    minutes = int(minutes_input)

    #Las horas obtenidas de los minutos
    hours = minutes // 60

    #Los minutos restantes
    minutes_rest = minutes % 60

    print(f"Me diste {minutes} minutos, y eso son {hours} horas y {minutes_rest} minutos.")

except ValueError:
    print("No es un número entero.")