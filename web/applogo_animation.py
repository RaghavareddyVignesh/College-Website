import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(6)  # Set the drawing speed

# Function to draw the letters
def draw_letter(letter, size, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(letter, align="center", font=("Arial", size, "bold"))

# Draw the letters "SunSense"
draw_letter("S", 40, -100, 0)
draw_letter("u", 40, -60, 0)
draw_letter("n", 40, -20, 0)
draw_letter("S", 40, 20, 0)
draw_letter("e", 40, 60, 0)
draw_letter("n", 40, 100, 0)
draw_letter("s", 40, 120, 0)
draw_letter("e", 40, 140, 0)
# Animate the logo
for _ in range(36):
    pen.clear()
    pen.left(10)  # Rotate the logo by 10 degrees
    # Redraw the letters at their new positions
    draw_letter("S", 40, -100, 0)
    draw_letter("u", 40, -60, 0)
    draw_letter("n", 40, -20, 0)
    draw_letter("S", 40, 20, 0)
    draw_letter("e", 40, 60, 0)
    draw_letter("n", 40, 100, 0)
    draw_letter("s", 40, 120, 0)
    draw_letter("e", 40, 140, 0)
    screen.update()  # Update the screen

# Hide the turtle and display the final logo
pen.hideturtle()
screen.mainloop()
