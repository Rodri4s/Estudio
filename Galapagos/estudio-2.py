import galapagar
import turtle

NUMERO_DE_ESTUDIO = 2
ANCHURA_VENTANA = 500
ALTURA_VENTANA = 500

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)

    #Se define la tortuga y sus caracteristicas
    miky = turtle.Turtle()
    miky.color("green")
    miky.pensize(5)
    miky.shape("turtle")
    ancho = 100
    alto = 50

    #Se definen las esquinas: para ajustar la esquina recuerda agregar o restar el length de la figura
    ANCHO_FIG = ANCHURA_VENTANA/4
    ALTO_FIG = ALTURA_VENTANA/4
    esquinas = [(-ANCHO_FIG,ALTO_FIG),(ANCHO_FIG,ALTO_FIG),(ANCHO_FIG,-ALTO_FIG),(-ANCHO_FIG,-ALTO_FIG)]

    #Dibuja un cuadrado en cada esquina generada por la lista y usando la funcion creada en galapagar.py
    for i in esquinas:
        miky.penup()
        miky.goto(i)
        miky.pendown()
        galapagar.rectangle(miky,ancho,alto)

    galapagar.finish(the_window)

main()
