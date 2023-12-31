#author:hanshiqiang365


import turtle as t
import pygame
import time

t.setup(700,470)

t.bgcolor("#29435c")

t.title("花好月圆 - 韩思工作室 - 祝各位朋友中秋快乐！")

time.sleep(5)
pygame.mixer.init()
pygame.mixer.music.load("..//turtle_mooncack//moonlight.wav")
pygame.mixer.music.play(-1)


#月亮
t.penup()
t.goto(160,-80)
t.color("#fdcb38")
t.pendown()
t.begin_fill()
t.circle(130)
t.end_fill()


#月亮里的小圆1
t.penup()
t.goto(232,-10)
t.color("#fcb937")
t.pendown()
t.begin_fill()
t.circle(38)
t.end_fill()


#月亮里的小圆2
t.penup()
t.goto(90,-30)
t.color("#fcb937")
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()


#月亮里的小圆3
t.penup()
t.goto(180,120)
t.color("#fcb937")
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()




#月饼
t.penup()
t.goto(-200,100)
t.pensize(5)
t.color("#eeaf22","#ffd982")
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()


#花瓣1
t.penup()
t.goto(-200,100)
t.setheading(-90)
r=8
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣2
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣3
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣4
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣5
t.penup()
t.left(180)
t.forward(2*r)
t.right(90)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣6
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣7
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣8
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣9
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣10
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣11
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣12
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣13
t.penup()
t.left(180)
t.forward(2*r)
t.right(70)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣14
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣15
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣16
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣17
t.penup()
t.left(180)
t.forward(2*r)
t.right(60)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣18
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣19
t.penup()
t.left(180)
t.forward(2*r)
t.right(80)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()
#花瓣20
t.penup()
t.left(180)
t.forward(2*r)
t.right(70)
t.pendown()
t.begin_fill()
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.end_fill()


t.penup()
t.setheading(0)
t.goto(-200,110)
t.pensize(3)
t.color("#eeaf22","#ffd982")
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()


t.penup()
t.goto(-200,120)
t.pensize(2)
t.color("#eeaf22","#ffd982")
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()


t.penup()
t.goto(-220,130)
t.left(45)
t.pendown()
t.forward(60)


t.penup()
t.goto(-218,142)
t.setheading(135)
t.pendown()
r=-18
t.circle(r,180)
t.left(90)
t.forward(2*r)
t.penup()
t.goto(-206,156)
t.setheading(135)
t.pendown()
t.forward(30)


t.penup()
t.goto(-208,132)
t.setheading(135)
t.pendown()
r=-18
t.circle(r,-180)
t.left(90)
t.forward(2*r)
t.penup()
t.goto(-196,146)
t.setheading(-45)
t.pendown()
t.forward(30)


#星星1
t.setheading(0)
t.pensize(1)
t.penup()
t.goto(-300,50)
t.left(20)
t.color("#f5df7c")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(20)
    t.left(144)
t.end_fill()
#星星2
t.penup()
t.goto(-160,20)
t.left(-20)
t.color("#f5df7c")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.left(144)
t.end_fill()
#星星3
t.penup()
t.goto(-60,90)
t.left(-10)
t.color("#f5df7c")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(26)
    t.left(144)
t.end_fill()
#星星4
t.penup()
t.goto(-110,224)
t.left(0)
t.color("#f5df7c")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(20)
    t.left(144)
t.end_fill()


#星星5
t.penup()
t.goto(265,200)
t.left(-20)
t.color("#f5df7c")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(24)
    t.left(144)
t.end_fill()
#星星6
t.penup()
t.goto(280,-100)
t.left(20)
t.color("#f5df7c")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(22)
    t.left(144)
t.end_fill()


#亮点1
t.penup()
t.goto(-340,220)
t.color("#ffffff")
t.pendown()
t.dot(5)
#亮点2
t.penup()
t.goto(-300,120)
t.color("#ffffff")
t.pendown()
t.dot(10)
#亮点3
t.penup()
t.goto(-226,10)
t.color("#ffffff")
t.pendown()
t.dot(8)
#亮点4
t.penup()
t.goto(-140,80)
t.color("#ffffff")
t.pendown()
t.dot(6)
#亮点5
t.penup()
t.goto(-110,120)
t.color("#ffffff")
t.pendown()
t.dot(6)
#亮点6
t.penup()
t.goto(20,18)
t.color("#ffffff")
t.pendown()
t.dot(10)
#亮点7
t.penup()
t.goto(0,140)
t.color("#ffffff")
t.pendown()
t.dot(4)
#亮点8
t.penup()
t.goto(100,200)
t.color("#ffffff")
t.pendown()
t.dot(8)
#亮点9
t.penup()
t.goto(320,120)
t.color("#ffffff")
t.pendown()
t.dot(8)
#亮点10
t.penup()
t.goto(230,-120)
t.color("#ffffff")
t.pendown()
t.dot(6)
#亮点11
t.penup()
t.goto(260,-90)
t.color("#ffffff")
t.pendown()
t.dot(4)
#亮点12
t.penup()
t.goto(320,-130)
t.color("#ffffff")
t.pendown()
t.dot(4)


#大兔子
t.setheading(0)
t.penup()
t.goto(-50,-210)
t.color("#ffffff")
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-56,-130)
t.color("#ffffff")
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()
t.goto(-70,-80)
t.setheading(60)
t.pendown()
t.begin_fill()
t.circle(30,80)
t.setheading(240)
t.circle(30,80)
t.end_fill()
t.penup()
t.goto(-50,-80)
t.setheading(40)
t.pendown()
t.begin_fill()
t.circle(30,80)
t.setheading(220)
t.circle(30,80)
t.end_fill()


#小兔子
t.setheading(0)
t.penup()
t.goto(-142,-190)
t.color("#ffffff")
t.pendown()
t.begin_fill()
t.circle(35)
t.end_fill()


t.penup()
t.goto(-138,-130)
t.color("#ffffff")
t.pendown()
t.begin_fill()
t.circle(24)
t.end_fill()


t.penup()
t.goto(-138,-90)
t.setheading(60)
t.pendown()
t.begin_fill()
t.circle(26,80)
t.setheading(240)
t.circle(26,80)
t.end_fill()


t.penup()
t.goto(-130,-88)
t.setheading(40)
t.pendown()
t.begin_fill()
t.circle(26,80)
t.setheading(220)
t.circle(26,80)
t.end_fill()


#底部圆弧
t.penup()
t.goto(-350,-80)
t.setheading(0)
t.color("#486e93")
t.pendown()
t.begin_fill()
t.circle(-200, 40) 
t.circle(300, 70)
t.setheading(20)
t.circle(-200, 80)
t.setheading(-90)
t.forward(30)
t.right(90)
t.forward(712)
t.end_fill()


t.done()