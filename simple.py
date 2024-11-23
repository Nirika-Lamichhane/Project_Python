import turtle

# Create a turtle screen
screen = turtle.Screen()

# Set up the screen properties
screen.setup(width=800, height=600)
screen.title("Turtle Drawing")

# Get ready to draw
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Keep the window open until closed by the user
screen.mainloop()
