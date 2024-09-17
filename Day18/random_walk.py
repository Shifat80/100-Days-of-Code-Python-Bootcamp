import random
import turtle as t


def random_color() -> tuple[int, int, int]:
    """Return a random RGB tuple."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


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
direction = [0, 90, 180, 270]

tim = t.Turtle()
t.colormode(255)

tim.pensize(15)
tim.speed("slowest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
def random_color():
    r=random.choice(0,255)
    g=random.choice(0,255)
    b=random.choice(0,255)
    random_color=(r,g,b)
    return random_color

colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","StateGray","SeaGreen"]
direction=[0,90,180,270]
tim.pensize(15)
tim.speed("slowest")
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
    
