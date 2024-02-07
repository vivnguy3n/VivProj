#Problem A, B, and C Simulating Gravity
import turtle, random, math
class Game:
    '''
    Purpose: (What does an object of this class represent?): This class represents how the actual game is run. It contains the class where all the entities of the 'game'
    will be implemented and manipulated. This class is meant to set up the game screen. 
    Instance variables: (What are the instance variables for this class, and what does each represent in a few words?)
        - self = the instance variable for this class as it has access to the class attributes, variables, and methods in the defined class. 
    Methods: (What methods does this class have, and what does each do in a few words?)
        - __init__ = it initializes the attributes of the objects in the class
        - player = represents the 'player' or the 'rocket'
        - gameloop = represents the players movement and prints out the result when it successfully lands or crashes into something.
    '''

    def __init__(self):
        #Bottom left corner of screen is (0, 0)
        #Top right corner is (500, 500)
        turtle.setworldcoordinates(0, 0, 500, 500)
        turtle.bgcolor('black')

        #INTRO
        txt = turtle.Turtle()
        txt.hideturtle()
        txt.penup()
        txt.goto(250, 250)
        txt.color("light coral", 'light pink')
        txt.write("WELCOME TO THE SLAY-CRAFT \U0001F485 \u2728:", align="center", font=("Garamond", 24, "bold"))
        txt.goto(250, 200)
        turtle.delay(3000)
        txt.write('\u2B50Try to navigate around any astroids!\u2B50', align = 'center', font=('Garamond', 24, 'bold' ))
        turtle.delay(1000)

        txt.clear() 
        # delay before starting the game
        turtle.delay(1000)

        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.delay(0)

        self.player = SpaceCraft(random.uniform(100,400), random.uniform(250, 450), random.uniform(-4, 4), random.uniform(-2, 0))
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_turn, 'Left')
        turtle.onkeypress(self.player.right_turn, 'Right')


        self.obstacle = []
        for i in range(10):
            obstacle = Obstacles()
            self.obstacle.append(obstacle)

        #"Stars"
        for i in range(50):
            px = random.randint(0, 500)
            py = random.randint(0, 500)
            size = random.randint(3, 4)
            turtle.penup()
            turtle.goto(px, py)
            turtle.dot(size, "light yellow")
    

        self.gameloop()
       
        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

    
    def gameloop(self):
        self.player.move()
        if self.player.xcor() < 0 or self.player.xcor() > 500 or self.player.ycor() < 0 or self.player.ycor() > 500 :
            wallcrash = turtle.Turtle()
            wallcrash.hideturtle()
            wallcrash.penup()
            wallcrash.goto(250, 250)
            wallcrash.color("white")
            wallcrash.write("You crashed into a wall..\U0001F611", align="center", font=("Comic Sans MS", 20, "bold"))
            return 
        if self.player.ycor() < 20: 
            if -3 >= self.player.vx <= 3 and -3 >=self.player.vy <= 3:
                success = turtle.Turtle()
                success.hideturtle()
                success.penup()
                success.goto(250, 250)
                success.color("white")
                success.write("Successful landing!! Here is your cookie\U0001f36a", align="center", font=("Comic Sans MS", 20, "bold"))
            else:
                crash = turtle.Turtle()
                crash.hideturtle()
                crash.penup()
                crash.goto(250, 250)
                crash.color("white")
                crash.write("You crashed \u2620", align="center", font=("Comic Sans MS", 20, "bold"))
            return 
        #Collisions
        for obstacle in self.obstacle:
            if self.player.distance(obstacle) < 15: 
                rip = turtle.Turtle()
                rip.hideturtle()
                rip.penup()
                rip.goto(250, 250)
                rip.color("white")
                rip.write("You crashed into an astroid. WOMP WOMP", align="center", font=("Comic Sans MS", 20, "bold"))
                return
            obstacle.move()
        
        turtle.ontimer(self.gameloop, 30)
        

class SpaceCraft(turtle.Turtle):
    '''
    Purpose: (What does an object of this class represent?)- This class represents the making of the spacecraft and what it can do. 
    Instance variables: (What are the instance variables for this class, and what does each represent in a few words?)
        - self = the instance variable for this class as it has access to the class attributes, variables, and methods in the defined class.
        - px = represents the spacecraft's position x value
        - py = represents the spacecraft's position y value
        - vx = represents the spacecraft's velocity x value
        - vy = represents the spacecraft's velocity y value
    Methods: (What methods does this class have, and what does each do in a few words?)
        - __init__ = it initializes the attributes of the objects in the class
        - move = represents the movement of the spacecraft
        - thrust = allows the spacecraft to be moved up and uses the "fuel"
        - left_turn = allows the spacecraft to be turned left and uses the "fuel"
        - right_turn = allows the spacecraft to be turned right and uses the "fuel"
    '''

    def __init__(self, px, py, vx, vy): 
        turtle.Turtle.__init__(self)
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.fuel = 40
        self.left(90)
        self.penup()
        self.speed(0)
        self.color('coral', 'yellow')
        self.goto(px, py)
        self.turtlesize(2,2,2)
    def move(self): 
        self.vy -= 0.0486
        px = self.xcor() + self.vx
        py = self.ycor() + self.vy
        self.goto(px, py) 
    def thrust(self):
        if self.fuel > 0:
            self.fuel -= 1
            angle = math.radians(self.heading())
            self.vx += math.cos(angle)
            self.vy += math.sin(angle)
            print("Number of fuel units remaining:", self.fuel)
        else: 
            print('Out of fuel!')

    def left_turn(self): 
        if self.fuel > 0: 
            self.fuel -= 1
            self.left(15)
            print('Fuel remaining:', self.fuel)
        else:
            print('Out of fuel!')
    def right_turn(self): 
        if self.fuel > 0:
            self.fuel -= 1
            self.right(15)
            print('Fuel remaining:', self.fuel)
        else:
            print('Out of fuel!')

#Problem D: Obstacles
class Obstacles(turtle.Turtle):
    '''
    Purpose: (What does an object of this class represent?)- This class represents the movement and the design of the obstacles in the game. 
    Instance variables: (What are the instance variables for this class, and what does each represent in a few words?)
        - self = the instance variable for this class as it has access to the class attributes, variables, and methods in the defined class.
    Methods: (What methods does this class have, and what does each do in a few words?)
        - __init__ = it initializes the attributes of the objects in the class
        - move = represents the movement of the obstacles in the game. 
    '''
    def __init__(self):
        turtle.Turtle.__init__(self)
        shapes = ['square', 'turtle', 'triangle']
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.shape(random.choice(shapes))
        self.color('medium aquamarine', 'plum')
        self.speed(0)
        self.shapesize(3,3,3)
        self.penup()
        self.goto(random.uniform(50, 400), random.uniform(10, 450))
        self.vx= 3
        self.vy = 3

        #Sun
        sun = turtle.Turtle()
        sun.color('gold')
        sun.penup()
        sun.goto(300, 400)
        sun.begin_fill()
        sun.shape('circle')
        sun.shapesize(5, 5, 5)
        sun.end_fill()
        sun.pendown()

        #random moon
        moon = turtle.Turtle()
        moon.color('grey')
        moon.penup()
        moon.goto(200, 300)
        moon.begin_fill()
        moon.shape('circle')
        moon.shapesize(3, 3, 3)
        moon.end_fill()
        moon.pendown()
        moon2 = turtle.Turtle()
        moon2.color('light grey')
        moon2.penup()
        moon2.goto(200, 300)
        moon2.begin_fill()
        moon2.shape('circle')
        moon2.shapesize(2, 2, 2)
        moon2.end_fill()
        moon2.pendown()
        moon3 = turtle.Turtle()
        moon3.color('white smoke')
        moon3.penup()
        moon3.goto(200, 300)
        moon3.begin_fill()
        moon3.shape('circle')
        moon3.shapesize(1, 1, 1)
        moon3.end_fill()
        moon3.pendown()
    #Move the obstacles
    def move(self):
        newvx = self.xcor() + self.vx
        newvy = self.ycor() + self.vy
        self.goto(newvx, newvy)
        if self.xcor() > 500 or self.xcor() < 0:
            self.vx *= -1
        if self.ycor() > 500 or self.ycor() < 0:
            self.vy *= -1

if __name__ == '__main__':
    Game()
