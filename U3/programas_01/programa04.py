import math

# --- FUNCIONES DE CÁLCULO ---

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura


# --- FUNCIONES DE INTERFAZ Y VALIDACIÓN ---

def mostrar_menu():
    print("\n----------------------------------------")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
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
                print("El radio no puede ser negativo ni cero. Vuelve a intentarlo.")
        except ValueError:
            print("Error: Debes introducir un valor numérico válido.")

def opcion2():
    while True:
        try:
            base = float(input("Introduce la base del triángulo: "))
            if base <= 0:
                print("La base debe ser mayor que 0. Introduce los datos de nuevo.")
                continue
            
            altura = float(input("Introduce la altura del triángulo: "))
            if altura <= 0:
                print("La altura debe ser mayor que 0. Introduce los datos de nuevo.")
                continue
            
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos válidos.")

def opcion3():
    while True:
        try:
            base = float(input("Introduce la base del rectángulo: "))
            if base <= 0:
                print("La base debe ser mayor que 0. Introduce los datos de nuevo.")
                continue
            
            altura = float(input("Introduce la altura del rectángulo: "))
            if altura <= 0:
                print("La altura debe ser mayor que 0. Introduce los datos de nuevo.")
                continue
            
            area = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area:.2f}")
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos válidos.")


# --- FUNCIÓN PRINCIPAL ---

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
            print("Saliendo del programa.")
            break
        else:
            print("Opción fuera de rango (1-4).")
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")

