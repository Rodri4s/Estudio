import galapagar

NUMERO_DE_ESTUDIO = 3
ANCHURA_VENTANA = 500
ALTURA_VENTANA = 500

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)

    miky = galapagar.defineTurtle("green",5,"turtle")
    an = 100
    al = 50

    #Se definen las esquinas: para ajustar la esquina recuerda agregar o restar el length de la figura
    ANCHO_FIG = ANCHURA_VENTANA/4
    ALTO_FIG = ALTURA_VENTANA/4
    esquinas = [(-ANCHO_FIG,ALTO_FIG),(ANCHO_FIG,ALTO_FIG),(ANCHO_FIG,-ALTO_FIG),(-ANCHO_FIG,-ALTO_FIG)]

    
    #Dibuja un cuadrado en cada esquina generada por la lista y usando la funcion creada en galapagar.py
    for i in esquinas:
        miky.penup()
        miky.goto(i)
        miky.pendown()
        galapagar.rectangle(miky,an,al)

    galapagar.finish(the_window)

main()
