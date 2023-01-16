import turtle

def draw_polygon(t, num_sides, side_length, color, fill_color):
    t.color(color)
    t.begin_fill()
    t.fillcolor(fill_color)
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)
    t.end_fill()

def main():
    num_sides = int(input("Enter the number of sides of the polygon: "))
    side_length = int(input("Enter the length of the side of the polygon: "))
    color = input("Enter the color of the polygon: ")
    fill_color = input("Enter the fill color of the polygon: ")
    
    t = turtle.Turtle()
    wnd = turtle.Screen()
    draw_polygon(t, num_sides, side_length, color, fill_color)
    wnd.exitonclick()

if __name__ == "__main__":
    main()
