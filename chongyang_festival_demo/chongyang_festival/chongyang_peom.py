#author:hanshiqiang365

import turtle
import time
import pygame


def drawMoon():            	#绘制太阳
  turtle.penup()   		#画笔拿起
  turtle.goto(-150, 0)
  turtle.fillcolor((255, 0, 0))   #太阳的颜色
  turtle.pendown()   		#画笔放下
  turtle.begin_fill()
  turtle.circle(112)
  turtle.end_fill() 		#颜色填充

def drawCloud():           	#绘制云朵
   turtle.penup()
   turtle.goto(-500, 200)
   turtle.fillcolor((245, 245, 245))
   turtle.pencolor((255, 255, 255))
   turtle.pensize(5)
   turtle.pendown()
   turtle.forward(250)
   def cloud(mode='right'):
      for i in range(90):
         turtle.pensize((i+1)*0.2+5)
         turtle.right(1) if mode == 'right' else turtle.left(1)
         turtle.forward(0.5)
      for i in range(90):
         turtle.pensize(90*0.2+5-0.2*(i+1))
         turtle.right(1) if mode == 'right' else turtle.left(1)
         turtle.forward(0.5)
   cloud()
   turtle.forward(100)
   cloud('left')
   turtle.forward(600)

def drawMountain():          	#绘制山川
   turtle.penup()
   turtle.goto(-500, -250)
   turtle.pensize(4)
   turtle.fillcolor((36, 36, 36))
   turtle.pencolor((31, 28, 24))
   turtle.pendown()
   turtle.begin_fill()
   turtle.left(20)
   turtle.forward(400)
   turtle.right(45)
   turtle.forward(200)
   turtle.left(60)
   turtle.forward(300)
   turtle.right(70)
   turtle.forward(300)
   turtle.goto(500, -300)
   turtle.goto(-500, -300)
   turtle.end_fill()

def initTurtle():
   pygame.mixer.init()
   pygame.mixer.music.load('chongyang_peom.mp3')
   pygame.mixer.music.play(-1, 20.0)
   turtle.hideturtle()
   turtle.setup(1000, 600)
   turtle.title('岁岁重阳，今又重阳 - 韩思工作室 - 祝各位朋友重阳节快乐！')
   turtle.colormode(255)
   turtle.bgcolor((193, 210, 240))
   turtle.speed(1)
   time.sleep(5)

def writePoetry():
  turtle.penup()
  turtle.goto(400, -150)
  turtle.pencolor((250, 240, 230))
  # 诗句
  potery = ["\n岁\n岁\n重\n阳\n", "今\n又\n重\n阳\n"]
  # 诗句位置(可自行设计添加), 最好2/4句五言诗
  coordinates = [(300, -150), (200, -150), (100, -150)]
  for i, p in enumerate(potery):
    turtle.write(p, align="center", font=("STXingkai", 50, "bold"))
    if (i + 1) != len(potery):
      time.sleep(2)
      turtle.goto(coordinates[i])

def main():
    initTurtle()
    drawMoon()          #绘制太阳
    drawCloud()         #绘制云朵
    drawMountain()      #绘制山
    writePoetry()       #写诗
    turtle.done()

if __name__ == '__main__':
    main()

