from TurtleWorld import *
bob = Turtle()

def koch(t, n):   #draw koch of length n with turtle
    if n<3:
        fd(t, n)
        return
    else:
        koch(t, n/3)
        lt(t, 60)
        koch(t, n/3)
        rt(t, 120)
        koch(t, n/3)
        lt(t, 60)
        koch(t, n/3)


def snowflake(t, n):
    for i in range(3)
        koch(t, n)
        rt(t, 60)
