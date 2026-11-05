import math

'''
'''

# --- FUNCIONES DE CÁLCULO ---

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura



def mostrar_menu():
    print("\n----------------------------------------")
    print("1. Calcular el área de un círculo[cite: 18]")
    print("2. Calcular el área de un triángulo[cite: 18]")
    print("3. Calcular el área de un rectángulo[cite: 18]")
    print("4. Salir[cite: 18]")
    print("----------------------------------------")

def opcion1():
    while True:
        try:
            radio = float(input("Introduce el radio del círculo: "))
            if radio > 0:
                area = calcular_area_circulo(radio)
                print(f"-> El área del círculo es: {area:.2f}")
                break
            else:
                print("Aviso: El radio debe ser mayor que 0.")
        except ValueError:
            print("Error: Introduce un valor numérico válido.")

def opcion2():
    while True:
        try:
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            if base > 0 and altura > 0:
                area = calcular_area_triangulo(base, altura)
                print(f"-> El área del triángulo es: {area:.2f}")
                break
            else:
                print("Aviso: La base y la altura deben ser mayores que 0.")
        except ValueError:
            print("Error: Introduce valores numéricos válidos.")

def opcion3():
    while True:
        try:
            base = float(input("Introduce la base del rectángulo: "))
            altura = float(input("Introduce la altura del rectángulo: "))
            if base > 0 and altura > 0:
                area = calcular_area_rectangulo(base, altura)
                print(f"-> El área del rectángulo es: {area:.2f}")
                break
            else:
                print("Aviso: La base y la altura deben ser mayores que 0.")
        except ValueError:
            print("Error: Introduce valores numéricos válidos.")


# FUNCIÓN PRINCIPAL 

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Introduce una opción (1-4): "))
            
            if opcion == 1:
                opcion1()
            elif opcion == 2:
                opcion2()
            elif opcion == 3:
                opcion3()
            elif opcion == 4:
                print("Saliendo del programa. ¡Hasta pronto!")
                break
            else:
                print("Error: Opción fuera de rango. Debe ser un número entre 1 y 4.")
                
        except ValueError:
            print("Error: Entrada no válida. Introduce un número entero del 1 al 4.")

if __name__ == "__main__":
    main()