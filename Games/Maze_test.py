import turtle
import numpy as np

#Creates the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('A Maze Game')
wn.setup(700,700)

#Create white pen with triangle shapes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('triangle')
        self.color('white')
        self.penup()
        self.speed(0)
#Inherit Pen class and change to green cirlce colors        
class Pen2(Pen):
    def __init__(self):
        super(Pen2,self).__init__()
        self.color('green')
        self.shape('circle')
class Pen3(Pen):
    def __init__(self):
        super(Pen3,self).__init__()
        self.color('blue')
        self.shape('square')
        
#Visualized Level
levels = [
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XX XXXXXXX          XXXXX',
'X  XXXXXXX  XXXXXX  XXXXX',
'X       XX  XXXXXX  XXXXX',
'X       XX  XXX        XX',
'XXXXXX  XX  XXX        XX',
'XXXXXX  XX  XXXXXX  XXXXX',
'XXXXXX  XX    XXXX  XXXXX',
'X  XXX        XXXX  XXXXX',
'X  XXX  XXXXXXXXXXXXXXXXX',
'X         XXXXXXXXXXXXXXX',
'X                XXXXXXXX',
'XXXXXXXXXXXX     XXXXX  X',
'XXXXXXXXXXXXXXX  XXXXX  X',
'XXX  XXXXXXXXXX         X',
'XXX                     X',
'XXX         XXXXXXXXXXXXX',
'XXXXXXXXXX  XXXXXXXXXXXXX',
'XXXXXXXXXX              X',
'XX   XXXXX              X',
'XX   XXXXXXXXXXXXX  XXXXX',
'XX    YXXXXXXXXXXX  XXXXX',
'XX          XXXX        X',
'XXXX                    X',
'XXXXXXXXXXXXXXXXXXXXXXXXX']

#Creates Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Gets the X and Y coordinates of the maze
            character = level[y][x]
            #Calculates the screen coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            #Checks if the positions to be stamped
            #if character == 'X':
            if character % 4 == 0:
                pen.goto(screen_x, screen_y)
                pen.stamp()
            elif character % 7 == 0:
                pen2.goto(screen_x, screen_y)
                pen2.stamp()
            elif character % 9 == 0:
                pen3.goto(screen_x, screen_y)
                pen3.stamp() 
    #Closes Turtles            
    turtle.done()
    turtle.bye()
                
                
pen = Pen()
pen2 = Pen2()
pen3 = Pen3()

#Creates a random level
levels_1 = np.random.randint(10, size=625).reshape(25,25)
setup_maze(levels_1)
#setup_maze(levels)

while True:
    pass

