import turtle

def draw_regular_polygon(t, sides, length, pos=(0,0), pen_color="black", fill_color=None, heading=0):
    """Draw a regular polygon centered at pos (approx)."""
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()
    if fill_color:
        t.color(pen_color, fill_color)
        t.begin_fill()
    else:
        t.color(pen_color)
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    if fill_color:
        t.end_fill()
    t.penup()

def draw_rectangle(t, width, height, pos=(0,0), pen_color="black", fill_color=None, heading=0):
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()
    if fill_color:
        t.color(pen_color, fill_color)
        t.begin_fill()
    else:
        t.color(pen_color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    if fill_color:
        t.end_fill()
    t.penup()

def main():
    screen = turtle.Screen()
    screen.title("Polygons - Equilateral Triangle, Rectangle, Hexagon")
    screen.bgcolor("#0f1720")        # background color
    screen.setup(width=1000, height=600)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(6)
    t.pensize(2)

    # Equilateral triangle (side ~140)
    # position so triangle sits left
    t.penup()
    t.goto(-380, 0)
    t.pendown()
    draw_regular_polygon(t, sides=3, length=140, pos=(-380, 0), pen_color="#ffffff", fill_color="#16a34a", heading=0)

    # Rectangle (center)
    draw_rectangle(t, width=240, height=120, pos=(-120, -60), pen_color="#ffffff", fill_color="#3b82f6", heading=0)

    # Hexagon (side ~70) on right
    draw_regular_polygon(t, sides=6, length=80, pos=(260, -40), pen_color="#ffffff", fill_color="#ef4444", heading=0)

    # Optional labels
    t.goto(-380, -110)
    t.color("#ffffff")
    t.write("Equilateral Triangle", align="center", font=("Arial", 10, "normal"))
    t.goto(0, -140)
    t.write("Rectangle", align="center", font=("Arial", 10, "normal"))
    t.goto(260, -120)
    t.write("Hexagon", align="center", font=("Arial", 10, "normal"))

    # Keep window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()