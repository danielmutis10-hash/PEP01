# Definición de la función con 4 parámetros de entrada y el valor por defecto "2DAW"
def saludar(nombre, primer_apellido, segundo_apellido, curso="2DAW"):
    print(f"Hola {nombre} {primer_apellido} {segundo_apellido}! Estás cursando {curso}.")


# --- INVOCACIONES DE PRUEBA ---

# 1
saludar("Daniel", "Mutis", "Guerrero")

# 2
saludar("Ana", "García", "López", "1DAW")

# 3
saludar(nombre="Carlos", primer_apellido="Pérez", segundo_apellido="Gómez", curso="2DAW")

# 4
saludar(segundo_apellido="Martín", nombre="Lucía", primer_apellido="Ruiz", curso="1DAW")