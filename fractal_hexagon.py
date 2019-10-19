#turtle Graphics in Pygame

#init
import turtle
turtle.setup(1024, 1024)
t = turtle.Turtle()
t.color('black', 'black')
t.pensize(1)
t.shape('arrow')
t.speed(1)

#setting up window
l=200
a=l/2
turtle.setup(6*a, 6*a)
t.penup()
t.left(180)
t.forward(a)
t.left(90)
t.forward(a)
t.pendown()

#fractal
def hexagon(size):
    for i in [1,2,3,4,5,6]:
        t.forward(size)
        t.left(60)

def hex_fractal2(size, min, ratio):
    if size>min:
        for i in [1,2,3,4,5]:
            hex_fractal2(size*ratio, min, ratio)
            t.left(120)
            t.forward(size*(1-ratio) )
    else:
        t.right(60)
        for i in [1,2,3,4,5]:
            t.forward(size)
            t.left(60)
        t.right(180)

def hex_fractal(size, min, ratio):
    for i in [1,2,3,4,5,6]:
        hex_fractal2(size*ratio, min, ratio)
        t.forward(size*(1-ratio))

hex_fractal(l, 25, 0.25)

def hexagon_ratio(length, ratio):
    a=length
    hexagon(a)
    a=a*ratio
    t.right(120)
    hexagon(a)

def fractal2(size,min):
    if size>min:
        t.right(90)
        for i in [1,2,3]:
            fractal2(size/2,min)
            t.right(90)
            t.forward(size/2)
    else:
            t.forward(size)
            t.left(90)
            t.forward(size)
            t.left(90)
            t.forward(size)
def fractal(size,min):
    t.begin_fill()
    for i in [1,2,3,4]:
        fractal2(size/2,min)
        t.right(90)
        t.forward(size/2)
    t.end_fill()

turtle.done()