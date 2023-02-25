
#To get started with games , import module
import turtle
import time
import winsound

#will create a window
wn = turtle.Screen()
wn.title("Pong by Bhawana")
wn.bgcolor("Black")
wn.setup(width=800,height=600)

#tracer--If n is 0 (zero), automatic screen updates are off.
# If n is 1 (one), the default, automatic screen updates will happen
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
#turtle. Turtle() is the constructor method of the class Turtle ; it returns an instance of the class turtle
paddle_a = turtle.Turtle()

#You can speed up or slow down the turtle's animation speed.
# (Animation controls how quickly the turtle turns and moves forward).
# Speed settings can be set between 1 (slowest) to 10 (fastest).
# But if you set the speed to 0, it has a special meaning — turn off animation and go as fast as possible.'''
paddle_a.speed(0)

paddle_a.shape("square") #by default 20x20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #it stretches the square of pong
#penup() makes sure that the moving object that you've created does not draw anything on the window.
paddle_a.penup()

#the location of the paddle_a on the game console screen
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") #by default 20x20 pixels
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #it stretches the square of pong
paddle_b.penup()
paddle_b.goto(350,0)


#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #by default 20x20 pixels
ball.color("white")
#paddle_b.shapesize(stretch_wid=5,stretch_len=1) #no stretch needed
ball.penup()
ball.goto(0,0)
ball.dx = 2 #this means everytime ball moves it moves 2pixels, dx is +2 means ,moves to right 2pixels
ball.dy = -2 #dy is +2 , so ball moves up +2pixels
#combining dx,dy , it moves diagonally +2 in both x&y (2,2)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #so you can move turtle without leaving tracks.
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align = "center",font =("Courier",24,"normal"))



#Creating function--
def paddle_a_up():
    #ycor returns y coordinate
    y= paddle_a.ycor()
    y+=20 #(y goesup when added)
    paddle_a.sety(y)

def paddle_a_down():
    #ycor returns y coordinate
    y= paddle_a.ycor()
    y-=20 #(y goesup when added)
    paddle_a.sety(y)

def paddle_b_up():
    #ycor returns y coordinate
    y= paddle_b.ycor()
    y+=20 #(y goesup when added)
    paddle_b.sety(y)

def paddle_b_down():
    #ycor returns y coordinate
    y= paddle_b.ycor()
    y-=20 #(y goesup when added)
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #Listen for keyboard input
wn.onkeypress(paddle_a_up,"w") #when user press w, calls for paddle_a_up.it would go up
wn.onkeypress(paddle_a_down,"s") #keyboard listens and when user presses s it goes down
wn.onkeypress(paddle_b_up,"Up") #when user press w, calls for paddle_a_up.it would go up
wn.onkeypress(paddle_b_down,"Down") #keyboard listens and when user presses s it goes down


#main game loop

while True:
    #every time loop runs , it updates the screen
    wn.update()


    #Move the ball

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    time.sleep(0.01)
    #Border checking
    #we had set the wn height to 600 , so 300upwards,300 downwards
    if ball.ycor()>290: #if ball goes above 290 y cooridnate ,
        ball.sety(290) #it bounces back to 290
        ball.dy *=-1 #this will reverse the direction of the ball (-2)
        winsound.PlaySound("metal-ping-192khz-3-86910.mp3",winsound.SND_ASYNC)

    if ball.ycor()<-290: #if ball goes below 290 y coordinate , it bounces back
        ball.sety(-290) #it goes to -290
        ball.dy *=-1   #and moves in +ve direction (by +2 pixels)
        winsound.PlaySound("metal-ping-192khz-3-86910.mp3", winsound.SND_ASYNC)

    if ball.xcor()>390: #if ball goes to the right more than 390 x coordinate ,
        ball.goto(0,0) #it bounces back to (0,0)
        ball.dx *=-1 #and then it goes to -ve direction(by -2 pixels)
        score_a+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:  # if ball goes to the left more than 390 x coordinate ,
        ball.goto(0,0)  # it bounces back to (0,0)
        ball.dx *= -1 # it goes +2 like (2,2)
        score_b+=1
        pen.clear() #to avoid overwriting scores
        pen.write("Player A:{} Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor() +40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340) #set ball bckwards to left at 340
        ball.dx *=-1
        winsound.PlaySound("metal-ping-192khz-3-86910.mp3", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor() +40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340) #set ball bckwards to left at 340
        ball.dx *=-1
        winsound.PlaySound("metal-ping-192khz-3-86910.mp3", winsound.SND_ASYNC)