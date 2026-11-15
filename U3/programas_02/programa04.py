import turtle

# Inicializamos la pantalla y la tortuga
t = turtle.Turtle()
t.speed(3)


#Cuadrado rojo sin rellenar
t.penup()
t.goto(-150, 0)#Nos movemos a la izquierda para organizar el espacio
t.pendown()

t.pencolor("red")#Color del trazo
t.pensize(3)#Grosor de la línea

#Bucle para dibujar los 4 lados del cuadrado
for _ in range(4):
    t.forward(100)#Avanza 100 píxeles
    t.right(90)#Gira 90 grados a la derecha

#Círculo verde relleno

t.penup()
t.goto(100, -50)
t.pendown()

t.pencolor("green")#Color del borde del círculo
t.fillcolor("green")#Color del relleno interior

t.begin_fill()#Indicamos el inicio del relleno
t.circle(50)#Dibujamos un círculo con radio de 50 píxeles
t.end_fill()#Cerramos y aplicamos el relleno de color

# Mantiene la ventana abierta hasta que el usuario la cierre
turtle.done()