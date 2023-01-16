"""Código para realizar los ejercicios de la asignatura Fundamentos de
Programación del grado en Ingeniería de Robótica Software de nombre:
"Estudios sobre abstracción funcional para Python y cuarteto de galápagos"
"""

import turtle

def init(title, color, width, height):
    """
    Crea una ventana para poder dibujar con el módulo de python turtle

    Parámetros: título, color de fondo, ancho y alto de la ventana creada
    Devuelve: la ventana creada.
    """

    window = turtle.Screen()
    turtle.setup(width, height)
    window.bgcolor(color)
    window.title(title)

    return window

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(360/4)

def rectangle(t, ancho, alto):
    for i in range(2):
        t.forward(ancho)
        t.left(90)
        t.forward(alto)
        t.left(90)

def defineTurtle(color, pensize, shape):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(pensize)
    t.shape(shape)
    return t

def finish(window):
    """
    Espera a que se haga click en window para cerrar la ventana.
    Se debe llamar al final de un programa que use turtle.

    Parámetros: una ventana creada por init()
    """

    window.exitonclick()
