from turtle import *


def rectangle_easy():
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    done()


def rectangle_profy():
    for _ in range(4):
        fd(100)
        lt(90)
    done()

def draw_n_angle(n):
    for _ in range(n):
        fd(100)
        left(360/n)
    done()

def draw_star(angle, n):
    for _ in range(n):
        fd(100)
        lt(angle)
    done()

# rectangle_easy()
#rectangle_profy()
#draw_n_angle(7)
draw_star(110,36)
