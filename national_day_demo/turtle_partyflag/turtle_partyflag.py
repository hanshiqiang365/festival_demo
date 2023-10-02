#author:hanshiqiang365

import turtle as t
import math
import pygame
import time

t.title('中华民族伟大复兴 - 韩思工作室 - 祝各位朋友国庆节快乐！')
t.setup(500,600)
t.speed(1)
t.penup()

# 背景音乐
time.sleep(5)
pygame.mixer.init()
pygame.mixer.music.load("国歌.mp3")
pygame.mixer.music.play(-1)

# 边框函数。从边框左上角顶点开始，turtle向右相对转向角度为90，循环四次单边并填充颜色，完成边框。

def Frame(startpoint):
    t.goto(startpoint)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("red")
    t.fd(300)
    t.right(90)
    t.fd(200)
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(200)
    t.right(90)
    t.end_fill()
    t.penup()

def FiveStar(startpoint,angle,forward_distance):
    t.goto(startpoint)
    t.pendown()
    t.setheading(angle)
    t.begin_fill()
    t.color("yellow")
    for i in range(5):
        t.fd(forward_distance)
        t.right(144)
    t.end_fill()
    t.penup()

#边框
Frame((-150,250))

#锤头
#输入转换为画布坐标系后的各点坐标
E = (25*28/12-350/3,25*0/12+475/3)
F = (25*32/12-350/3,25*4/12+475/3)
G = (25*7.5/12-350/3,25*14.5/12+475/3)
H = (25*18.5/12-350/3,25*25.5/12+475/3)
I = (25*3/12-350/3,25*19/12+475/3)
J = (25*16/12-350/3,25*28/12+475/3)
L = (25*((57-177**0.5)/4)/12-350/3,25*((121-177**0.5)/4)/12+475/3)
K = (25*12.5/12-350/3,25*32/12+475/3)
alpha = (25*10.5/12-350/3,25*17.5/12+475/3)
beta = (25*14.5/12-350/3,25*21.5/12+475/3)
# JK 距离
JK = ((25*16/12-350/3-(25*12.5/12-350/3))**2+(25*28/12+475/3-(25*32/12+475/3))**2)**0.5
# LJ圆弧角度
LJdegree = math.degrees(math.atan(((177**0.5-7)/4)/((177**0.5+7)/4))) + math.degrees(math.atan(7/8))

#连接并填充颜色
t.begin_fill()
t.color('yellow')
t.goto(E)
t.pd()
t.goto(alpha)
t.goto(G)
t.goto(I)
t.goto(L)
t.setheading(-math.degrees(math.atan(((177**0.5-7)/4)/((177**0.5+7)/4))))   # 绝对角度turtle转向至LK圆的相切方向
t.circle(JK,LJdegree)   # 以K为圆心，LK为半径，画弧LJ
t.goto(H)
t.goto(beta)
t.goto(F)
t.goto(E)
t.end_fill()
t.pu()

#镰刀
# 输入转换为画布坐标系后的各点坐标
M = (25*16/12-350/3,25*16/12+475/3)
N = (25*16/12-350/3,25*32/12+475/3)
O = (25*16/12-350/3,25*0/12+475/3)
P = (25*16/12-350/3,25*18/12+475/3)
Q = (25*((27-623**0.5)/2)/12-350/3,25*((41-623**0.5)/2)/12+475/3)
R = (25*10/12-350/3,25*16.5/12+475/3)
S = (25*(10+276.25**0.5)/12-350/3,25*16.5/12+475/3)
T = (25*15.5/12-350/3,25*16.5/12+475/3)
U = (25*15.5/12-350/3,25*(22-276.25**0.5)/12+475/3)
V = (25*28/12-350/3,25*0/12+475/3)
W = (25*3.5/12-350/3,25*10.5/12+475/3)
X = (25*2.5/12-350/3,25*2.5/12+475/3)
Y = (25*5/12-350/3,25*3/12+475/3)
Z = (25*3/12-350/3,25*5/12+475/3)
delta1 = (25*(16-9*2**0.5)/12-350/3,25*(18-9*2**0.5)/12+475/3)
delta2 = (25*((6+34**0.5)/4)/12-350/3,25*((14+34**0.5)/4)/12+475/3)
theta1 = (25*(18-158**0.5)/12-350/3,25*(16-158**0.5)/12+475/3)
theta2 = (25*((14+34**0.5)/4)/12-350/3,25*((6+34**0.5)/4)/12+475/3)

# 计算各个半径
MN = 16*(25/12)
PO = 18*(25/12)
RN = 276.25**0.5*(25/12)
TS = (276.25**0.5-5.5)*(25/12)
VU = 276.25**0.5*(25/12)
VW = VU
TU = TS
RS = RN
XX = 2.5*(25/12)

# 计算各个圆弧角度
NOdegree = 180
OQdegree = math.degrees(math.atan((16-(-(2*(524+45*623**0.5)/299)))/18))
NSdegree = math.degrees(math.atan(15.5/6))
SUdegree = 90
UWdegree = math.degrees(math.atan(12/11.5))
ZYdegree = 2*math.degrees(math.asin(2**0.5/2.5))
delta2theta2degree =  360-(2*(math.degrees(math.acos((34**0.5-4)/10))-45))

t.setheading(0)
t.goto(N)
t.pd()
t.begin_fill()
t.color('yellow')
t.circle(-MN,NOdegree)
t.circle(-PO,OQdegree)
t.goto(W)
t.setheading(-UWdegree)
t.circle(VW,UWdegree)
t.circle(TU,SUdegree)
t.circle(RS,NSdegree)
t.pu()

t.goto(delta1)
t.pd()
t.goto(delta2)
t.setheading(-(90-math.degrees(math.acos((34**0.5-4)/10))))   # 绝对角度turtle转向至X圆的相切方向
t.circle(-XX,-delta2theta2degree)
t.goto(delta2)
t.goto(theta2)
t.goto(theta1)
t.goto(delta1)
t.end_fill()
t.pu()


#五星红旗
#边框
Frame((-150,-50))
FiveStar((-100,-70),-72,60*math.cos(18*math.pi/180))
FiveStar((-50-50*math.sqrt(34)/34,-70-30*math.sqrt(34)/34),18+math.degrees(math.atan(3/5)),20*math.cos(18*math.pi/180))
FiveStar((-30-7*math.sqrt(2),-90-math.sqrt(2)),18+math.degrees(math.atan(1/7)),20*math.cos(18*math.pi/180))
FiveStar((-30-70*math.sqrt(53)/53,-120+20*math.sqrt(53)/53),18-math.degrees(math.atan(2/7)),20*math.cos(18*math.pi/180))
FiveStar((-50-50*math.sqrt(41)/41,-140+40*math.sqrt(41)/41),18-math.degrees(math.atan(4/5)),20*math.cos(18*math.pi/180))

t.hideturtle()
t.goto(-220,-10)
t.color('red')
t.write("祝伟大祖国生日快乐！1949 - 2023", font=("繁体隶书", 20, "bold"))

t.done()



