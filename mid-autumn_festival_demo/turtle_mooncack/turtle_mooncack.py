#author:hanshiqiang365

from turtle import *
import pygame
import time

hideturtle()
colormode(255)

setup(1000,800,0,0)
title('Moon Cack drawed by hanshiqiang365 - Happy Mid-Autumn Festival')

time.sleep(5)
pygame.mixer.init()
pygame.mixer.music.load("moonlight.wav")
pygame.mixer.music.play(-1)

def MoonCake(bgcolor, mkcolor, wdcolor, words):

    pensize(2)
    pencolor(0, 0, 0)
    fillcolor(bgcolor)

    begin_fill()

    for i in range(12):
        if i == 5:
            p = pos()
        circle(30, 120)
        right(90)
    end_fill()

    penup()
    fd(20)
    pendown()

    fillcolor(mkcolor)

    begin_fill()

    for i in range(12):
        circle(30, 120)
        right(90)
    end_fill()

    pencolor(wdcolor)

    left(90)
    fd(140)
    left(90)
    fd(140)
    left(90)
    fd(72)

    p = pos()

    wd1 = words[0:2]
    wd2 = words[2:4]

    write(wd1, font=("繁体隶书", 58, "bold"))
    fd(70)
    write(wd2, font=("繁体隶书", 58, "bold"))

    left(90)
    fd(140)

    penup()
    goto(-280, -350)
    pendown()
    write('【韩思工作室2023年出品：祝各位朋友中秋快乐！】', font=("繁体隶书", 18, "bold"))


MoonCake((235, 63, 125), (255, 16, 125), (205, 138, 125), '韩思月饼')
#MoonCake((63, 231, 162), (16, 255, 166), (58, 204, 22), '韩思月饼')

#MoonCake((231, 162, 63), (255, 166, 16), (204, 22, 58), '五仁月饼')
#MoonCake((97, 154, 195),(186, 204, 217) ,(17, 101, 154), '冰皮月饼')


mainloop()

