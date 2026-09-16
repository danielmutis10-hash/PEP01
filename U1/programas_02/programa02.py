#Primero creamos la variable que contendrá el número entero 6
var_1 = 6

#Escritura del tipo de objeto del numero 6 y la variable creada
print(type(6), type(var_1))

#Varaible 2 que tiene el valor de la primera
var_2 = var_1

#Al igual que la primera variable con el objeto pero en este caso con la segunda
print(type(6), type(var_2))

#Comprobamos con is e is not las variables
print(f"{var_1} o sea var_1 es igual a la var_2:  {var_1 is var_2}")
print(f"{var_1} o sea var_1 es distinta a la var_2:  {var_1 is not var_2}")

#Asignarle a var_1 "Hola"
var_1 = "Hola"

#Escribir que "Hola" es del mismo tipo de var_1 ahora que se le ha cambiado
print(f'"Hola" es un {type("Hola")} al igual que "var_1" que es {type(var_1)} y distintos del número entero 6 que es {type(6)}')
print(" ")

#Uso de la funcion isinstance()
if (isinstance(var_1, type("Hola"))):
    print(f'{var_1} o sea "var_1" es una variable de tipo {type(var_1)}')
    print(f'a diferencia de "var_2" que es una variable de tipo {type(6)}')
elif (isinstance(var_1, type(6))):
    print(f'{var_1} o sea "var_1" es una variable de tipo {type(6)}')
    print(f'a diferencia de "var_2" que es una variable de tipo {type("Hola")}')