import turtle
import math

a = 300.0
b = 3 / 5 * a * math.sin(math.pi/5) / math.sin(3*math.pi/10)


# window = turtle.Screen()
# window.bgcolor("white")
# window.title("Happy VietNam Independence Day")
# window.setup(1000, 800, -900, 50)

t = turtle.Turtle()
t.up()
t.goto(-3*a/2, a)
t.down()
t.color("red")
t.begin_fill()

for i in range(2):
    t.forward(3*a)
    t.right(90)
    t.forward(2*a)
    t.right(90)

t.end_fill()
t.up()
t.goto(0, 3*a/5)
t.down()
t.speed(2)

t.color("yellow")
t.begin_fill()

t.right(72)
for i in range(5):
    t.forward(b)
    t.left(72)
    t.forward(b)
    t.right(144)
    

t.end_fill()

t.hideturtle()
turtle.done()