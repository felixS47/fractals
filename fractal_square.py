#turtle Graphics in Pygame

#init
import turtle
turtle.setup(1024, 1024)
t = turtle.Turtle()
t.color('black', 'black')
t.pensize(1)
t.shape('arrow')
t.speed(0)
t.hideturtle()

#setting up window
l=256
a=l/2
turtle.setup(6*a, 6*a)
t.penup()
t.left(180)
t.forward(a)
t.left(90)
t.forward(a)
t.pendown()

#fractal

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

fractal(l,4)

#for min in [128,64,32,16,8,4,2]:
    #fractal(l,min)



turtle.done()