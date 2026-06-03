"""
Brian Casey

Project 3 Refactoring Improvements:
I updated my Project 2 turtle scene by breaking the large draw_scene function
into smaller functions with single responsibilities, such as drawing the
sun, clouds, house, tree, bush, and flower. I also removed repeated code by
creating reusable functions for objects like clouds and windows.
This made the program easier to read, maintain, and extend, which allowed me
to create a scene much more easily.
"""

import turtle
import math


def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw a triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """Draw a curved line using small line segments"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    segment_length = length / segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)

    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


# ----------------------------
# Smaller helper functions
# ----------------------------

def draw_grass(t):
    """Draw the grass/ground"""
    jump_to(t, -400, 120)
    t.setheading(0)
    draw_rectangle(t, 800, 260, "lightgreen")


def draw_sun(t, x, y, radius=40):
    """Draw the sun with rays"""
    jump_to(t, x, y)
    t.setheading(0)
    draw_circle(t, radius, "gold")

    for angle in range(0, 360, 45):
        jump_to(t, x, y + radius)
        t.setheading(angle)
        t.forward(18)
        t.backward(36)


def draw_cloud(t, x, y):
    """Draw a reusable cloud made of 4 circles"""
    offsets = [(0, 0), (30, 15), (60, 0), (30, -15)]
    for dx, dy in offsets:
        jump_to(t, x + dx, y + dy)
        t.setheading(0)
        draw_circle(t, 20, "white")


def draw_window_with_cross(t, x, y, size=30):
    """Draw one window with cross bars"""
    jump_to(t, x, y)
    t.setheading(0)
    draw_square(t, size, "lightyellow")

    jump_to(t, x + size / 2, y)
    t.setheading(270)
    t.forward(size)

    jump_to(t, x, y - size / 2)
    t.setheading(0)
    t.forward(size)


def draw_house(t, x, y):
    """Draw a house with roof, door, knob, and two windows"""
    # house body
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, 160, 110, "wheat")

    # roof
    jump_to(t, x - 20, y)
    t.setheading(0)
    draw_triangle(t, 200, "firebrick")

    # door
    jump_to(t, x + 62, y - 35)
    t.setheading(0)
    draw_rectangle(t, 35, 75, "saddlebrown")

    # doorknob
    jump_to(t, x + 70, y - 75)
    t.setheading(0)
    draw_circle(t, 3, "gold")

    # windows
    draw_window_with_cross(t, x + 25, y - 35)
    draw_window_with_cross(t, x + 105, y - 35)


def draw_tree(t, x, y):
    """Draw a tree with trunk and leafy top"""
    # trunk
    jump_to(t, x, y)
    t.setheading(0)
    draw_rectangle(t, 25, 60, "sienna")

    # leaves
    for dx, dy in [(-5, 5), (25, 5), (10, -20)]:
        jump_to(t, x + dx, y + dy)
        t.setheading(0)
        draw_circle(t, 28, "forestgreen")


def draw_bush(t, x, y):
    """Draw a bush"""
    jump_to(t, x, y)
    t.setheading(0)
    draw_polygon(t, 6, 22, "green")


def draw_flower(t, x, y):
    """Draw a flower with stem, petals, and center"""
    t.pencolor("green")
    jump_to(t, x, y)
    t.setheading(270)
    t.forward(35)

    t.pencolor("black")
    for dx, dy in [(10, -10), (-10, -10), (-10, 10), (10, 10)]:
        jump_to(t, x + dx, y + dy)
        t.setheading(0)
        draw_circle(t, 7, "pink")

    jump_to(t, x, y)
    draw_circle(t, 9, "yellow")


# ----------------------------
# Scene functions
# ----------------------------

def draw_original_scene(t):
    """Draw the original Project 2 scene"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")
    t.pensize(2)
    t.color("black")

    draw_grass(t)
    draw_sun(t, 250, 220)
    draw_cloud(t, -230, 210)
    draw_cloud(t, 40, 180)
    draw_house(t, -110, 120)
    draw_tree(t, 90, 60)
    draw_bush(t, 160, 145)
    draw_flower(t, 200, 80)


def draw_enhanced_scene(t):
    """Draw a more populated scene using the same reusable functions"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")
    t.pensize(2)
    t.color("black")

    draw_grass(t)
    draw_sun(t, 250, 220)

    # more clouds
    draw_cloud(t, -260, 220)
    draw_cloud(t, -40, 200)
    draw_cloud(t, 140, 185)

    # original house area
    draw_house(t, -110, 120)
    draw_tree(t, 90, 60)
    draw_bush(t, 160, 145)
    draw_flower(t, 200, 80)

    # added items to show reusability
    draw_tree(t, -260, 70)
    draw_tree(t, 250, 70)

    draw_bush(t, -180, 150)
    draw_bush(t, -150, 145)
    draw_bush(t, 210, 145)

    draw_flower(t, -210, 90)
    draw_flower(t, -170, 95)
    draw_flower(t, 140, 90)
    draw_flower(t, 230, 95)


# YOU MUST add function calls in this draw_scene function definition
# to create your scene (No statements outside of function definitions)
def draw_scene(t):
    """Display the original scene first"""
    draw_original_scene(t)


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()