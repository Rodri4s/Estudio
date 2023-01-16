import galapagar
import turtle

NUMERO_DE_ESTUDIO = 1
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():
    #Inicia los parametros del programa
    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO), "lightgray", ANCHURA_VENTANA, ALTURA_VENTANA)

    #Se define la tortuga y sus caracteristicas
    miky = turtle.Turtle()
    miky.color("red")
    length = 50

    #Para ajustar la esquina recuerda agregar o restar el length de la figura
    esquinas = [(-200-length,200+length),(200+length,200+length),(200+length,-200-length),(-200-length,-200-length)]

    #Dibuja un cuadrado en cada esquina generada por la lista y usando la funcion creada en galapagar.py
    for i in esquinas:
        miky.penup()
        miky.goto(i)
        miky.pendown()
        galapagar.square(miky,length)

    #Finalizar programa
    galapagar.finish(the_window)


main()
