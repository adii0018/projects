import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)

# Colors list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Spiral drawing
for i in range(200):
    t.pencolor(colors[i % 6])  # Change color
    t.forward(i * 2)
    t.right(59)

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()