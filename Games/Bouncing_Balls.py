import turtle
import random

#Starts the screen and intializes list variables
wn = turtle.Screen()
wn.bgcolor('gray')
wn.title('Bouncing Ball Simulator')
wn.tracer(0)
balls = []
colors = ['red', 'blue', 'yellow', 'orange', 'green', 'white', 'purple']
shapes = ['circle', 'triangle', 'square']

#Creates Balls
class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        self.penup()
        self.speed(0)
        self.goto(random.randint(-290,290), random.randint(200, 400))
        self.dy = 0
        self.dx = random.uniform(-0.75, 0.75)
        self.da = random.randint(-5, 5)
#Setting gravity
gravity = 0.001

#creating multiple balls
for _ in range(25):
    balls.append(Ball())

while True:
    wn.update()
    
    for ball in balls:
        #updates ball values
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
        #check for a wall
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.da *= -1
        if ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1
        #check for a bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1