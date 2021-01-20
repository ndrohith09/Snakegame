import turtle
import tkinter as Tk
import time
import random # for random movement of attributes

delay =0.1




#score initialization

score = 0

high_score = 0

wn =turtle.Screen()
wn.title("GARUDA SNAKE GAME")
wn.bgcolor("black")
#wn.bgpic("s16.gif")

#H=802 ,V=900

wn.setup(width=800,height =800)
wn.tracer(0)# turns off the screen updates


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("#6c27e3")
border_pen.penup()
border_pen.setposition(-370,-370) # pen position where the border starts to draw
border_pen.pendown()
border_pen.pensize(7)
for side in range (4):
    border_pen.fd(750) # 750 units distance
    border_pen.lt(90) # angle 
border_pen.hideturtle()



segments=[] # list to add segments

#snake head
head =turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#2ce655")
head.penup()  # penup is for lines
head.goto(0,0)
head.shapesize(1)
head.direction = "stop"


#turtle.register_shape("m.gif")
#snake food
food =turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#ff3636")
food.penup()
food.shapesize(0.8,0.8)
food.setheading(90)
food.goto(0,100)

# pen (score)
pen =turtle.Turtle()
pen.speed(0)
##pen.shape("triangle")
pen.color("#ffffff")
pen.penup()  # penup is for lines
pen.hideturtle()
pen.goto(0,340)  # score position
pen.write("SCORE:0    HIGH SCORE: 0",align = "center",font =("Algerian",22))  #font style 

Garuda =turtle.Turtle()
Garuda.speed(0)
Garuda.setposition(100,-350)
Garuda.color("#1690ab")
#Garuda.penup()  # penup is for lines
Garuda.penup()
Garuda.hideturtle()
Garuda.write("Garuda Works",font=("Capacitor" , 17))#Vijaya,capacitor,wide latin,aharoni,Almonte,comicsans
#functions
def go_up():
    if head.direction != "down": # whiling move up if you press down you cant go in reverse
        head.direction ="up"

def go_down():
    if head.direction != "up":
        head.direction ="down"

def go_left():
    if head.direction != "right": # whiling move left if you press right you cant go in right
        head.direction ="left"

def go_right():
    if head.direction != "left":
        head.direction ="right"


def move():
    if head.direction == "up": # going up direction
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down": # going down direction
        y=head.ycor()
        head.sety(y-20)

    if head.direction == "left": # going left direction
        x=head.xcor()
        head.setx(x-20)
    
    if head.direction == "right": # going right direction
        x=head.xcor()
        head.setx(x+20)

# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up") #for up arrow use Up  (onkeypress in pyton 3.7)
wn.onkeypress(go_down,"Down") #for down arrow use Down  (onkeypress in pyton 3.7)
wn.onkeypress(go_right,"Right") #for right arrow us Right   (onkey in pyton 2.7)
wn.onkeypress(go_left,"Left") #for left arrow use Left  (onkey in pyton 2.7)

 # main loop
while True:
    wn.update()

#move food to random spot
    if head.distance(food)<20:
        x = random.randint(-350, 350)  #moving position of food
        y = random.randint(-330, 350)
        food.goto(x,y)

# add segments(it remains static and new segment doesnt move)
        new_segment = turtle.Turtle()
        new_segment.speed(0)   #animation speed
        new_segment.shape("square") # next segment shape
        new_segment.color("#e6e32c") # color of new segment
        new_segment.shapesize(0.8,1)
        new_segment.setheading(270)
        segments.append(new_segment) 
        new_segment.penup()

#shorten the delay
        delay-=0.001

# increase score 
        score+=10

        if score> high_score:
            high_score= score

        pen.clear() 
        pen.write("SCORE: {}   HIGH SCORE: {}".format(score, high_score),align = "center",font =("Algerian",22,"normal "))  #font style   
        

# move the end segments first in reverse order.(it moves from 10 to 1)
    for index in range (len(segments)-1,0,-1):
        x= segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

# collision with border
    if  head.xcor()>357 or head.xcor()<-357 or head.ycor()>356 or head.ycor()<-356:
        time.sleep(1) #after one second it comes back to original position
        head.goto(0,0) # head goes to origin after collision
        head.direction= "stop"


# head collision
    for segment in segments:
        if segment.distance(head)<20: #they overlap
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
# to hide the segments of pre existing game
            for segment in segments:
                segment.goto(1000, 1000)

#clearing segments
            segments.clear()

            delay=0.1

#reset the score
            score=0

            delay=0.1
             
            pen.clear()
            pen.write("SCORE: {}   HIGH SCORE: {}".format(score, high_score),align = "center",font =("Algerian",20,"normal "))  #font style 
            Garuda.penup()



#move segment zero to where the head is
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    time.sleep(delay)

wn.mainloop()
