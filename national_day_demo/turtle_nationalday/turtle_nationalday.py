#author:hanshiqiang365

import turtle
import math
import pygame
import time

def draw_polygon(t, size=50, n=3):
    for i in range(n):
        t.forward(size)
        t.left(360.0 / n)


def draw_n_angle(t, size=50, num=5, color=None):
    if color:
        t.begin_fill()
        t.fillcolor(color)
    for i in range(num):
        t.forward(size)
        t.left(360.0 / num)
        t.forward(size)
        t.right(2 * 360.0 / num)
    if color:
        t.end_fill()


def draw_5_angle(t=None,
                 start_pos=(0, 0),
                 end_pos=(0, 10),
                 radius=100,
                 color=None):
    t = t or turtle.Turtle()
    # size = radius * math.sin(math.pi/5)/math.sin(math.pi*2/5)计算公式错误，但不影响显示
    size = radius * math.sin(math.pi / 5) / math.sin(math.pi * 3 / 10)  # 修正
    angle = math.degrees(
        math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0]))
    print(angle)
    t.penup()
    t.goto(start_pos)
    t.setheading(0)
    t.left(angle)
    t.fd(radius)
    t.pendown()
    t.right(math.degrees(math.pi * 9 / 10))
    draw_n_angle(t, size, 5, color)


def draw_5_star_flag(times=20.0):
    width, height = 30 * times, 20 * times
    # 初始化屏幕和海龟
    window = turtle.Screen()
    window.title("中华民族伟大复兴 - 韩思工作室 - 祝各位朋友国庆节快乐！")

    # 背景音乐
    time.sleep(8)
    pygame.mixer.init()
    pygame.mixer.music.load("国歌.mp3")
    pygame.mixer.music.play(-1)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(1)

    # 画红旗
    t.penup()
    t.goto(-width / 2, height / 2)
    t.pendown()
    t.begin_fill()
    t.fillcolor('red')
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.fd(width)
    t.right(90)
    t.fd(height)
    t.right(90)
    t.end_fill()
    # 画大星星
    draw_5_angle(t,
                 start_pos=(-10 * times, 5 * times),
                 end_pos=(-10 * times, 8 * times),
                 radius=3 * times,
                 color='yellow')
    # 画四个小星星
    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]
    for pos in stars_start_pos:
        draw_5_angle(t,
                     start_pos=(pos[0] * times, pos[1] * times),
                     end_pos=(-10 * times, 5 * times),
                     radius=1 * times,
                     color='yellow')

    t.penup()
    t.goto(-390, -350)
    t.pendown()
    t.color('red')
    t.write('祝伟大祖国生日快乐！1949 - 2023', font=("繁体隶书", 38, "bold"))

    # 点击关闭窗口
    window.exitonclick()

draw_5_star_flag()


