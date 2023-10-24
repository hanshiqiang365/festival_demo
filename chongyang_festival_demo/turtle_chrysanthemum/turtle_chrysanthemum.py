#author:hanshiqiang365

import turtle
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load('chongyang.wav')
pygame.mixer.music.play(-1, 20.0)

turtle.title('重阳节赏菊花 - 韩思工作室 - 祝各位朋友重阳节快乐！')
turtle.speed(0)
turtle.bgcolor('black')

time.sleep(10)
 
turtle.pencolor('orange')
turtle.fillcolor("yellow")
 
length = 20
angle = 120
turtle.penup()
 
for i in range(300):
    for j in range(4):
        length+=0.4
        if j==0:
            turtle.pendown()
        turtle.forward(length)
        turtle.left(angle)
        turtle.penup()
    turtle.left(3.6)
turtle.end_fill()
 
turtle.hideturtle()
turtle.done()

