from math import cos, pow, radians, sin, sqrt


def mostrar_menu():

    print("CALCULADORA MATEMÁTICA")
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")
    print("5. Salir")


while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción (1-5): "))

        if opcion == 1:
            angulo_grados = float(input("Introduce el ángulo (en grados): "))
            angulo_rads = radians(angulo_grados)
            resultado = sin(angulo_rads)
            print(f"-> El seno de {angulo_grados}° es: {resultado:.4f}")

        elif opcion == 2:

            angulo_grados = float(input("Introduce el ángulo (en grados): "))
            angulo_rads = radians(angulo_grados)
            resultado = cos(angulo_rads)
            print(f"El coseno de {angulo_grados}° es: {resultado:.4f}")

        elif opcion == 3:
            numero = float(
                input("Introduce el número para calcular su raíz cuadrada: ")
            )
            if numero < 0:
                print(
                    "No se puede calcular la raíz cuadrada de un número negativo en los números reales."
                )
            else:
                resultado = sqrt(numero)
                print(f"La raíz cuadrada de {numero} es: {resultado:.4f}")

        elif opcion == 4:
            base = float(input("Introduce la base: "))
            exponente = float(input("Introduce el exponente: "))
            resultado = pow(base, exponente)
            print(f"{base} elevado a {exponente} es: {resultado:.4f}")

        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción fuera de rango. Debe introducir un número entre 1 y 5.")

    except ValueError:
        print("Entrada no válida. Debe introducir un valor numérico correcto.")
