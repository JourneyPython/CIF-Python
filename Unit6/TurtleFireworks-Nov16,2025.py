import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_firework_body(x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.color("red")
    t.begin_fill()
    t.pendown()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()

def draw_fuse(start_x, start_y):
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(60)
    t.color("yellow")
    t.pensize(3)
    t.pendown()

    for _ in range(30):
        t.forward(2)
        t.right(2)

    return t.position()

def draw_ball_arc(start_x, start_y):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape("circle")
    ball.color("orange")
    ball.speed(0)
    ball.pensize(3)
    ball.penup()

    ball.goto(start_x, start_y)
    ball.setheading(70)

    for _ in range(20):
        ball.pendown()
        ball.forward(3)
        ball.left(1)

    for _ in range(20):
        ball.forward(3)
        ball.right(2)

    return ball.position()

def draw_explosion(x, y):
    t.penup()
    t.goto(x, y)
    t.color("yellow")
    t.pensize(2)

    for angle in range(0, 360, 30):
        t.setheading(angle)
        t.pendown()
        t.forward(70)
        t.penup()
        t.goto(x, y)

fire_x = -200
fire_y = -150
width = 80
height = 120

draw_firework_body(fire_x, fire_y, width, height)

fuse_end_x, fuse_end_y = draw_fuse(fire_x + width/2, fire_y + height)

explode_x, explode_y = draw_ball_arc(fuse_end_x, fuse_end_y)

draw_explosion(explode_x, explode_y)

turtle.done()
