#Dibuja varios cuadrados incrementando de tamaño
import turtle

def squares(t,length):
    for i in range(4):
        t.forward(length)
        t.left(360/4)

def increasingSquare(t,length):
    for i in range(5):
        squares(t, length)
        t.penup()
        t.backward(length/2)
        t.right(90)
        t.forward(length/2)
        t.left(90)
        t.pendown()
        length = length + length



def main():
    wnd = turtle.Screen()
    miky = turtle.Turtle()

    size = 20

    #squares(miky,size)
    increasingSquare(miky,size)
    wnd.exitonclick()

if __name__ == "__main__":
    main()