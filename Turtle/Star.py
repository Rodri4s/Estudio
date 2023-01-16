import turtle

def star(t,length):
    for i in range(5):
        t.forward(length)
        t.left(216)    

def main():
    mike = turtle.Turtle()
    wnd = turtle.Screen()
    
    size = 100
    
    star(mike,size)
    wnd.exitonclick()

if __name__ == "__main__":
    main()