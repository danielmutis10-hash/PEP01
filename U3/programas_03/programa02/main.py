import operaciones

def main():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        print("\n--- Resultados de las operaciones ---")
        print(f"Suma ({num1} + {num2}) = {operaciones.suma(num1, num2)}")
        print(f"Resta ({num1} - {num2}) = {operaciones.resta(num1, num2)}")
        print(f"Multiplicación ({num1} * {num2}) = {operaciones.multiplicacion(num1, num2)}")
        
        # recogemos el resultado en una variable
        res_division = operaciones.division(num1, num2)
        print(f"División ({num1} / {num2}) = {res_division}")
    except ValueError:
        print("Debes introducir obligatoriamente valores numéricos.")

if __name__ == "__main__":
    main()