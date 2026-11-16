from U3.programas_04.programa02.matematicas import area_triangulo, area_rectangulo, area_circulo, a_hexadecimal, a_entero, a_binario, suma, resta, multiplicacion, division



def main():
    while True:
        print("\n")
        print("---------MENÚ PRINCIPAL---------")
        print("1. Operaciones matemáticas")
        print("2. Cálculo de áreas geométricas")
        print("3. Conversiones numéricas")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            
            if opcion == 1:
                print("\nOPERACIONES MATEMÁTICAS")
                n1 = float(input("Introduce el primer número: "))
                n2 = float(input("Introduce el segundo número: "))
                print(f"- Suma: {suma(n1, n2)}")
                print(f"- Resta: {resta(n1, n2)}")
                print(f"- Multiplicación: {multiplicacion(n1, n2)}")
                print(f"- División: {division(n1, n2)}")
                
            elif opcion == 2:
                print("\nCÁLCULO DE ÁREAS")
                print("1. Rectángulo")
                print("2. Triángulo")
                print("3. Círculo")
                sub_op = int(input("Elige figura (1-3): "))
                
                if sub_op == 1:
                    b = float(input("Base: "))
                    h = float(input("Altura: "))
                    print(f"Área del rectángulo: {area_rectangulo(b, h)}")
                elif sub_op == 2:
                    b = float(input("Base: "))
                    h = float(input("Altura: "))
                    print(f"Área del triángulo: {area_triangulo(b, h)}")
                elif sub_op == 3:
                    r = float(input("Radio: "))
                    print(f"Área del círculo: {area_circulo(r)}")
                else:
                    print("Opción de figura no válida.")
                    
            elif opcion == 3:
                print("\nCONVERSIONES NUMÉRICAS")
                texto = input("Introduce un número entero para convertir: ")
                num_entero = a_entero(texto)
                
                if num_entero is not None:
                    print(f"- En binario: {a_binario(num_entero)}")
                    print(f"- En hexadecimal: {a_hexadecimal(num_entero)}")
                else:
                    print("El texto introducido no es un número entero válido.")
                    
            elif opcion == 4:
                print("Saliendo del programa.")
                break
            else:
                print("Opción fuera de rango (1-4).")
                
        except ValueError:
            print("Introduce un valor numérico entero para el menú.")


if __name__ == "__main__":
    main()