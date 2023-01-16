import turtle

def triangle(t,length):
    for i in range(3):
        t.forward(length)
        t.left(360/3)
    
def square(t,length):
    for i in range(4):
        t.forward(length)
        t.left(360/4)

def hexagon(t,length):
    for i in range(6):
        t.forward(length)
        t.left(360/6)    

def octagon(t,length):
    for i in range(8):
        t.forward(length)
        t.left(360/8)  

def main():
    mike = turtle.Turtle()
    wnd = turtle.Screen()
    
    size = 100
    
    triangle(mike,size)
    square(mike,size)
    hexagon(mike,size)
    octagon(mike,size)
    wnd.exitonclick()
    


if __name__ == "__main__":
    main()