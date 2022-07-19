import turtle  
from turtle import Screen, pen
import random
import time

screen = Screen()
screen.setup(400 + 4, 500 + 8) 


end = turtle.Turtle()
x = (-150, 150)
y = (150, 150)
end.penup()
end.goto(x)
end.pendown()
end.goto(y)
end.hideturtle()

n = 5
t = [turtle.Turtle(visible=False) for a in range(n)]
colors = []

for i in range(n):
    color = "%06x" % random.randint(0, 0xFFFFFF)
    colors.append(color)
    t[i].color('#'+color)
    t[i].shape('turtle')
    t[i].penup()
    t[i].goto(i*50-100, -200)
    t[i].left(90) 
    t[i].showturtle() 
    t[i].pendown()


race = True
while race:
    pos = []
    for i in range(n):
        t[i].forward(random.randint(1,5))
        pos.append(t[i].pos())
    for i in range(len(pos)):
        if pos[i][1] >= 150:
            race = False
            winner = i+1

turtle.hideturtle()
turtle.penup()
turtle.goto(-55, 200)
turtle.color('#'+colors[winner-1])
turtle.write("Winner "+str(winner), font=(None, 20))



turtle.mainloop()  