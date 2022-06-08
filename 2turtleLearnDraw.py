from turtle import *

color('red', 'yellow')


def draw_letter_m(barva):
    color(barva)
    left(90)
    forward(100)
    right(150)
    forward(70)
    left(120)
    forward(70)
    right(150)
    forward(100)
    done()


def draw_basic_line():
    fd(40)
    penup()
    fd(20)
    pendown()
    fd(40)
    done()


def draw_line_size(size):
    fd(70)
    color('red')
    pensize(size)
    fd(30)
    done()


def draw_line_dot():
    fd(50)
    penup()
    dot(5, 'green')
    fd(50)
    dot(5, 'green')
    done()


def draw_flag_fill():
    left(90)
    fd(50)
    begin_fill()
    fd(50)
    right(120)
    fd(50)
    right(120)
    fd(50)
    right(120)
    fd(50)
    end_fill()
    done()


def draw_czech_flag():
    color('black', 'white')
    begin_fill()
    for i in range(2):
        fd(200)
        lt(90)
        fd(100)
        lt(90)
    end_fill()

    color('red')
    begin_fill()
    for i in range(2):
        fd(200)
        lt(90)
        fd(50)
        lt(90)
    end_fill()

    color('blue')
    begin_fill()
    lt(30)
    fd(100)
    for i in range(2):
        lt(120)
        fd(100)
    end_fill()

    done()


# draw_letter_m('green')
# draw_basic_line()
# draw_line_size(3)
# draw_line_dot()
# draw_flag_fill()
draw_czech_flag()
