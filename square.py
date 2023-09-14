import turtle              # Allows us to use the turtle module
wn = turtle.Screen()       # Create a window for turtles
mike = turtle.Turtle()     # Create a turtle, assign to mike

mike.forward(50)           # Draw a square
mike.left(90)
mike.forward(50)
mike.left(90)
mike.forward(50)
mike.left(90)
mike.forward(50)
mike.left(90)

wn.mainloop()              # Wait for events, such as closing window
