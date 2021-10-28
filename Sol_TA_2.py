import turtle

n = int(input('Enter the no of the sides of the polygon : '))
side = int(input('Enter the length of the sides of the polygon : '))

def draw_polygon():
    for _ in range(n):
        turtle.forward(side)
        turtle.right(360 / n)

draw_polygon()

turtle.penup()
turtle.goto(80, 40)
turtle.pendown()

draw_polygon()
