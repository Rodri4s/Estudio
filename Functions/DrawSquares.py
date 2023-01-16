
#Dibuja 5 cuadrados en una fila hacia el lado derecho
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.pendown()
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(2*sz)
        
def nextSquares(t,sz):
    for i in range(5):
        drawSquare(t,sz)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("pink")
    alex.pensize(2)

    nextSquares(alex,20)
    wn.exitonclick()

if __name__ == "__main__":
    main()