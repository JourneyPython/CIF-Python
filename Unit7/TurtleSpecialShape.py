import turtle

screen = turtle.Screen()
screen.bgcolor("snow2")
t = turtle.Turtle()
t.speed(0)
t.color("light steel blue4")

def draw_circle(turtle_obj, size):
    for _ in range(2):
        turtle_obj.circle(size, 60)
        turtle_obj.left(120)
        turtle_obj.circle(size, 60)
        turtle_obj.left(120)

for i in range(33):
    t.width(i / 15 + 0.5)

    t.circle(100) 
    t.right(11) 

t.penup()

t.hideturtle()
turtle.done()