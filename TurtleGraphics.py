import turtle as garo
import random
from time import sleep


# Screen
garo.bgcolor("black")
garo.setup(width=1.0, height=1.0, )
garo.speed(0)

# Welcome Message Function
def welcome_msg():
    welcome = garo.Turtle()
    welcome.penup()
    welcome.goto(-300, 350)
    welcome.pendown()
    welcome.color("blue","black")
    welcome.stamp()
    welcome.write("A'chik Computer Programmer Turtle Graphics Program", font=("Arial", 17, "normal"))
    welcome.fd(550)
    welcome.stamp()
    welcome.penup()
    welcome.goto(-300, 320)
    welcome.pendown()
    welcome.color("red")
    welcome.stamp()
    welcome.write("Control kode, Instructions ingipa text file niko nibo ", font=("Arial", 17, "normal"))
    welcome.goto(-300, 320)
    welcome.fd(580)
    welcome.stamp()
    welcome.penup()
    welcome.goto(-300, 290)
    welcome.pendown()
    welcome.color("purple")
    welcome.stamp()
    welcome.write("Dao 10 seconds ni jamande Ia kattarang gimaigenok ", font=("Arial", 17, "normal"))
    welcome.goto(-300, 290)
    welcome.fd(550)
    welcome.stamp()
    welcome.penup()
    welcome.goto(-300, 260)
    welcome.pendown()
    welcome.color("green")
    welcome.stamp()
    welcome.write("Abachengna de mouse ko click kabo ", font=("Arial", 17, "normal"))
    welcome.goto(-300, 260)
    welcome.fd(550)
    welcome.stamp()
    welcome.penup()
    welcome.goto(-300, 260)
    welcome.hideturtle()
    sleep(12)
    welcome.clear()
    
welcome_msg()



colours = ["violet", "indigo", "blue", "green", "yellow", "grey", "black", "orange", "red"]
shapes = ["turtle", "circle", "arrow", "triangle", "square","classic"]



    




# Functions

def up():
    garo.setheading(90)
    garo.forward(50)

def down():
    garo.setheading(270)
    garo.forward(50)

def left():
    garo.setheading(180)
    garo.forward(50)

def right():
    garo.setheading(0)
    garo.forward(50)

def upper_left():
    garo.setheading(135)
    garo.forward(50)

def lower_left():
    garo.setheading(225)
    garo.forward(50)

def upper_right():
    garo.setheading(45)
    garo.forward(50)

def lower_right():
    garo.setheading(315) #315
    garo.forward(50)

def home():
    garo.home()

def clickleft(x, y):
    garo.color(random.choice(colours))

def clickright(x, y):
    garo.stamp()

def clickmiddle(x, y):
    garo.shape(random.choice(shapes))

def penup():
    garo.penup()
def pendown():
    garo.pendown()
def beginfill():
    garo.begin_fill()
def endfill():
    garo.end_fill()

def screencolor():
    garo.bgcolor(random.choice(colours))

def screen_undo():
    garo.undo()

def screen_clear():
    garo.clear()

def exit():
    garo.bye()

# Event Listening
garo.listen()




# Controls 

# Movements
garo.onkey(up, 'w')
garo.onkey(down, 's')
garo.onkey(left, 'a')
garo.onkey(right, 'd')
garo.onkey(upper_left, 'q')
garo.onkey(lower_left, 'z')
garo.onkey(upper_right, 'e')
garo.onkey(lower_right, 'c')
garo.onkey(home, 'x')

# Pen up, Pen down, 
garo.onkey(penup, '1')
garo.onkey(pendown, '2')

# Begin fill, End fill
garo.onkey(beginfill, '3')
garo.onkey(endfill, '4')

garo.onscreenclick(clickmiddle, 2)
garo.onscreenclick(clickleft, 1)
garo.onscreenclick(clickright, 3)

garo.onkey(screencolor, '5')
garo.onkey(screen_undo, '6')
garo.onkey(screen_clear, '7')



garo.onkey(exit, "o")
# Program Loop
garo.mainloop()

# exit = garo.mainloop(False) 
