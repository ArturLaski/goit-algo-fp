import turtle

def draw_pythagorean_tree(level, length, angle):
    if level == 0:
        turtle.forward(length)
        turtle.backward(length)
        return

    turtle.forward(length)
    turtle.left(angle)

    draw_pythagorean_tree(level - 1, length * 0.5, angle)

    turtle.right(2 * angle)
    
    draw_pythagorean_tree(level - 1, length * 0.5, angle)

    turtle.left(angle)
    turtle.backward(length)

# Initial setup
turtle.speed('fastest')
turtle.left(90)  # Start pointing up

# Draw the Pythagorean tree
draw_pythagorean_tree(5, 100, 45)  # Example: level 5, length 100, angle 45

# Complete the drawing
turtle.done()
