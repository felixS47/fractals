#init
import turtle
t = turtle.Turtle()
t.color('black', 'black')
t.pensize(1)
t.shape('arrow')
t.speed(0)

#setting up window
l=729
min=100
ratio=1/3
a=l/2

def hex2(size,min,ratio):
    t.right(120)
    if size>min:
        for i in [1,2,3,4,5]:
            hex2( size*ratio, min,ratio)
            t.right(180)
            t.forward( size*(1-ratio) )
            t.left(60)
    else:
        for i in [1,2,3,4,5]:
            t.forward(size)
            t.left(60)

def hex(size,min,ratio):
    t.begin_fill()
    for i in [1,2]:
        hex2(size*ratio,min,ratio)
        t.right(180)
        t.forward(size*(1-ratio) )
        t.left(60)
    t.end_fill()


t.right(19)
#for min in [96,48,24,12]:
hex(l,min,ratio)

turtle.done()