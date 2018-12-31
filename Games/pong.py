import turtle
import random

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Create Paddles
class Paddle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        
    def Paddle_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
        
    def Paddle_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class Ball(turtle.Turtle): 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.dx = random.sample([-0.2, 0.2], 1)[0]
        self.dy = random.sample([-0.2, 0.2], 1)[0]

paddle_a = Paddle()
paddle_a.goto(-350, 0)
paddle_b = Paddle()
paddle_b.goto(350, 0)
ball = Ball()

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a.Paddle_up, 'w')
wn.onkeypress(paddle_a.Paddle_down, 's')
wn.onkeypress(paddle_b.Paddle_up, 'Up')
wn.onkeypress(paddle_b.Paddle_down, 'Down')
#Main Game loop
while True:
    wn.update()
    
    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Boarder checking
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= random.sample([-1,1], 1)[0]
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= random.sample([-1,1], 1)[0]
        
    #check for a bounce
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= random.sample([-1,1], 1)[0]
        
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= random.sample([-1,1], 1)[0]
        
    #Paddle with ball collision
    if (ball.xcor()> 340 and ball.xcor()< 350) and (ball.ycor() < 
        paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() - 45):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor() < 
        paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() - 45):
        ball.setx(-340)
        ball.dx *= -1