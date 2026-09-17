fahrenheit_input = input("Dime los grados Fahrenheit que desees convertir a Celcius \n:")
try:

    fahrenheit = float(fahrenheit_input)

    celsius = (((fahrenheit - 32.0)*5)/9)
    print(f'Tus {fahrenheit} grados Fahrenheit son {celsius} grados Celsius')

except ValueError:
    print("El valor ingresado no es ni un decimal ni un entero")