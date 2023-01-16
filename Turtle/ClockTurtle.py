#Dibuja un reloj con estampillas de tortuga
import turtle

def drawLine(t,length, line, stamp):
    t.penup()
    t.forward(length)
    t.pendown()
    t.forward(line)
    t.penup()
    t.forward(stamp)
    t.stamp()

def returnCenter(t, length):
    t.penup()
    t.left(180)
    t.forward(length)

def drawNext(t,length,line,stamp,center):
    for j in range(6):
        for i in range(2):
            drawLine(t,length,line,stamp)
            returnCenter(t,center)
        t.right(30)



def main():
    mike = turtle.Turtle()
    wnd = turtle.Screen()

    mike.color("blue")
    mike.shape("turtle")
    
    size = 100
    line = size/10
    stamp = line*2
    center = size + line + stamp
    
    drawNext(mike,size,line,stamp,center)
    wnd.exitonclick()

if __name__ == "__main__":
    main()
