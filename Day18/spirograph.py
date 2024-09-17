import random
import turtle as t


def random_color() -> tuple:
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "StateGray",
    "SeaGreen",
]

tim = t.Turtle()
if tim is not None:
    t.colormode(255)
    tim.color(random_color())
    tim.circle(100)

    screen = t.Screen()
    screen.exitonclick()

import random
import turtle as t


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "StateGray",
    "SeaGreen",
]

tim = t.Turtle()
if tim is not None:
    t.colormode(255)
    tim.speed("fastest")
    for _ in range(200):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

    screen = t.Screen()
    screen.exitonclick()



