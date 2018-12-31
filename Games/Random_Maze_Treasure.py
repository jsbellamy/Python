import turtle
import numpy as np
import math

#Creates the screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('A Maze Game')
wn.setup(700,700)

#Create white pen with triangle shapes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
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
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('turtle')
        self.color('brown')
        self.penup()
        self.speed(0)
        self.gold = 0
    #Creates Movement Directions    
    def move_up(self):
        #calculate spot to move
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        #check is space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def move_down(self):
        #calculate spot to move
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        #check is space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def move_right(self):
        #calculate spot to move
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        #check is space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def move_left(self):
        #calculate spot to move
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        #check is space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        
        if distance < 5:
            return True
        else:
            return False
        
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

        
#Visualized Level
levels = [
'XXXXXXXXXXXXXXXXXXXXXXXXX',
'XP XXXXXXX          XXXXX',
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
            if character == 0:
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            elif character == 3:
                player.goto(screen_x, screen_y)
            elif character == 2:
                treasures.append(Treasure(screen_x, screen_y))
            #if character % 4 == 0:
                #pen.goto(screen_x, screen_y)
                #pen.stamp()
            #elif character % 7 == 0:
                #pen2.goto(screen_x, screen_y)
                #pen2.stamp()
            #elif character % 9 == 0:
                #pen3.goto(screen_x, screen_y)
                #pen3.stamp()
    
                
player = Player()                
pen = Pen()
#pen2 = Pen2()
#pen3 = Pen3()

#Creates a random level (different from visualized)
level_range = np.arange(1,24)
levels_1 = np.random.randint(1, size=625).reshape(25,25)
levels_1[np.ix_(level_range,level_range)] = np.random.choice(3, (23,23),
        p=[0.325, 0.665, .01])
levels_1[1,1] = 3
#Creates walls
walls = []
#Creates treasure
treasures = []
#starts the maze
setup_maze(levels_1)
#setup_maze(levels)
turtle.listen()
turtle.onkey(player.move_up, 'Up')
turtle.onkey(player.move_left, 'Left')
turtle.onkey(player.move_down, 'Down')
turtle.onkey(player.move_right, 'Right')

wn.tracer(0)

while True:
    #Check for player collision with treasure
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the gold to the player
            player.gold += treasure.gold
            print('Player Gold: {}'.format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            treasures.remove(treasure)
    wn.update()

