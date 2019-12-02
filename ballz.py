# Abdulaziz Alharqan's code

from tkinter.ttk import *
from tkinter import *
from random import randint, choice
from PIL import ImageTk, Image
import os
import math
from time import time

def randomBlockNumber(level):
    return randint(level, 2*level)
    
    

####################################
# customize these functions
####################################


TESTING = False # False is default; setting to True causes the ball to bounce off baseline (used while testing collisions)
WIDTH = 400
HEIGHT = 800
BLOCKSIZE = 40
INS = 2 # make the blocks slightly smaller in appearance
TIMERDELAY = 10
#main screen
class Main:
    def __init__(self, root):
        self.frame = Frame(root)
        img = ImageTk.PhotoImage(Image.open("Gametitle.png"))
        img2 = ImageTk.PhotoImage(Image.open("Playbutton1.png"))
        img3 = ImageTk.PhotoImage(Image.open("Shopbutton1.png"))
        Gamelabel = Label(self.frame, image = img, bg = "black")
        Gamelabel.image = img
        Gamelabel.pack()
        img2.image = img2
        img3.image = img3
        #playbtnimg = img2.subsample(3,2)
        #shopbtnimg = img3.subsample(3,2)
        self.play_button=Button(root, text="Start Game", image = img2 ,command = self.startGame, bg = "black")
        self.shop_button=Button(root, text="Shop", image = img3, command = self.openShop, bg = "black")
        self.frame.pack()
        #self.frameTitle.pack(padx=100,pady = 19)
        self.play_button.pack(padx = 25, pady = 9)
        self.shop_button.pack(padx = 25, pady = 7) 

    def startGame(self):
        btn = self.play_button
        if btn:
            self.frame.master.destroy()
            gamescreen = run(WIDTH, HEIGHT)
            
        else: 
            pass
    def openShop(self):
        btn = self.shop_button
        if btn:
            self.frame.master.destroy()
            window = Tk()
            window.geometry("2000x1500+300+100")
            window.wm_title("ballz (Shop)")
            shopscreen = Shop(window)
            window.mainloop()
        else:
            pass


class Shop:
    def __init__(self, root):
        self.frame = Frame(root)
        self.root = root
        img1 = ImageTk.PhotoImage(Image.open("Balls1.png"))
        img2 = ImageTk.PhotoImage(Image.open("Themes1.png"))
        img3 = ImageTk.PhotoImage(Image.open("Coins1.png"))
        canvas1 = Canvas(self.frame, width = 2000, height = 150, bg = "black")
        inner_canvas1 = Canvas(canvas1, width = 300, height = 100, bg = "black")
        canvas1.create_window(50, 30, anchor = NW, window = inner_canvas1)
        inner_canvas1.create_image(110, 65, anchor = CENTER, image = img1)
        inner_canvas1.image = img1
        inner_canvas2 = Canvas(canvas1, width = 300, height = 100, bg = "black")
        canvas1.create_window(1000, 30, anchor = W, window = inner_canvas2)
        inner_canvas2.create_image(110, 65, anchor = CENTER, image = img3)
        inner_canvas2.image = img3
        canvas2 = Canvas(self.frame, width = 2000, height = 250, bg = "grey")
        canvas3 = Canvas(self.frame, width = 2000, height = 150, bg = "black")
        inner_canvas3 = Canvas(canvas3, width = 300, height = 100, bg = "black")
        canvas3.create_window(50, 30, anchor = NW, window = inner_canvas3)
        inner_canvas3.create_image(90, 65, anchor = CENTER, image = img2)
        inner_canvas3.image = img2
        canvas4 = Canvas(self.frame, width = 2000, height = 250, bg = "grey")
        canvas1.pack()
        canvas2.pack()
        canvas3.pack()
        canvas4.pack()
        self.frame.pack()

class Explosion:
    def __init__(self, row, col, explosionFrames):
        self.row = row
        self.col = col
        self.explosionFrames = explosionFrames
        self.nFrames = len(self.explosionFrames)
        self.i = 0
        self.slowDownFactor = 3 # to slow down the explosion
        
    def __hash__(self):
        return hash(str(self.row) + "," + str(self.col))
        
    def draw(self, canvas):
        if self.i//self.slowDownFactor < self.nFrames:
            #canvas.create_image(self.col * BLOCKSIZE + 0.5*BLOCKSIZE, self.row * BLOCKSIZE + 0.5 * BLOCKSIZE, image=self.explosionFrames[self.i // self.factor])
            
            canvas.create_image(self.col * BLOCKSIZE + 0.5*BLOCKSIZE, self.row * BLOCKSIZE + 0.5 * BLOCKSIZE, image=self.explosionFrames[self.i // self.slowDownFactor])
            self.i += 1
            
    def isOver(self):
        return self.i//self.slowDownFactor == self.nFrames
    
#all block functionalities will be in this class
class Block:
    def __init__(self, row, col, number):
        colors = ['#279bc5', '#6fe9a2', '#ffd400', '#e10909', '#ff004e', '#e10982']
        self.row = row
        self.col = col
        self.color = choice(colors)
        self.number = number
      
    def getGridPosition(self):
        return self.row, self.col
        
    def moveDown(self):
        self.row += 1
        
    def offGrid(self):
        return self.row > HEIGHT//BLOCKSIZE
        
    def draw(self, canvas, data):
        x = data.blocksize * self.col
        y = data.blocksize * self.row
        canvas.create_rectangle(x + INS, y + INS, x + data.blocksize - INS, y + data.blocksize - INS, fill=self.color, outline="")
        canvas.create_text(x + 0.5 * data.blocksize, y + 0.5 * data.blocksize, text=str(self.number))


    def left(self):
        return BLOCKSIZE * self.col

    def right(self):
        return BLOCKSIZE * (self.col + 1)

    def bottom(self):
        return BLOCKSIZE * (self.row + 1)

    def top(self):
        return BLOCKSIZE * self.row

    

    def getRectangle(self):
        x = BLOCKSIZE * self.col
        y = BLOCKSIZE * self.row
        topLeft = x, y
        bottomRight = x + BLOCKSIZE, y + BLOCKSIZE
        topRight = x + BLOCKSIZE, y
        bottomLeft = x, y + BLOCKSIZE
        return [topLeft, topRight, bottomRight, bottomLeft]
        
#all the ball functionalities will be under this class     
class Ball:
    def __init__(self, x, y, angle):
        self.isMoving = True
        self.x = x
        self.y = y
        
        self.radius = 10
        self.speed = 10 # not changing for now
        self.setAngle(angle)
        #self.vx = 3
        #self.vy = 3
        #self.vx = 3
        #self.vy = -3 # as 10 and -10
        #self.prevGridCol = self.x // data.blocksize
        #self.prevGridRow = self.y // data.blocksize 
        self.prevGridRow = -1
        self.prevGridCol = -1
    
    
    def setAngle(self, angle):
        self.vx = self.speed * math.cos(angle)
        self.vy = -self.speed * math.sin(angle)
    
    def setMoving(self, isMoving):
        self.isMoving = isMoving
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def getPosition(self):
        return self.x, self.y

        
    
    def update(self, data):
        if self.isMoving:
            r = self.radius
            if self.x <= 2*r or self.x >= WIDTH-2*r:
                self.vx = -self.vx
            if self.y <= 2*r or self.y >= HEIGHT-2*r:
                self.vy = -self.vy
                
            self.x += self.vx
            self.y += self.vy
        
        # figure out which grid cell we are in
            col = int(self.x) // data.blocksize
            row = int(self.y) // data.blocksize
            if (row, col) in data.powerUpLocations:
                data.powerUpLocations.remove((row, col))
                data.nPowerUps += 1

            for rowNum in range(row-1, row+2):
                for colNum in range(col-1, col+2):
                    if (rowNum, colNum) in data.blocks:
                        block = data.blocks[(rowNum, colNum)]
                        
                        if self.intersects(block):
                            block.number -= 1
                            if block.number == 0:
                                del data.blocks[(rowNum, colNum)]
                                explosion = Explosion(rowNum, colNum, data.EXPLOSIONFRAMES)
                                data.explosions.add(explosion)
                                
                            if row != rowNum: # entered vertically
                                self.vy = -self.vy
                            if col != colNum:
                                self.vx = -self.vx
                                
            #if self.prevGridCol != col:
            self.prevGridCol = col
            #if self.prevGridRow != row:
            self.prevGridRow = row
                
        
    def left(self):
        return self.x - self.radius

    def right(self):
        return self.x + self.radius

    def top(self):
        return self.y - self.radius

    def bottom(self):
        return self.y + self.radius
 
                
                
    
    def intersects(self, block):
        return not (self.top() > block.bottom() or self.bottom() < block.top() or self.right() < block.left() or self.left() > block.right())
        
        
    #To draw the circle  
    def draw(self, canvas, data):
        canvas.create_oval(self.x-self.radius+INS, self.y-self.radius+INS, self.x+self.radius-INS, self.y+self.radius-INS, fill='white')

########
class PowerUp:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.innerRadius = 8
        self.outerRadius = 13
        self.outerMin = 10
        self.outerMax = 16
        self.width = 2
        self.x = (col + 0.5) * BLOCKSIZE
        self.y = (row + 0.5) * BLOCKSIZE
        self.increasing = True
    
    def moveDown(self):
        self.row += 1
        
    def offGrid(self):
        return self.row > HEIGHT//BLOCKSIZE
    
        
    def draw(self, canvas):
        if self.increasing and self.outerRadius >= self.outerMax:
            self.increasing = False
        elif not self.increasing and self.outerRadius <= self.outerMin:
            self.increasing = True
        if self.increasing:
            self.outerRadius += 0.5
        else:
            self.outerRadius -= 0.5
 
        canvas.create_oval(self.x-self.innerRadius, self.y-self.innerRadius, self.x+self.innerRadius, self.y+self.innerRadius, fill='white', outline='white')
        canvas.create_oval(self.x-self.outerRadius, self.y-self.outerRadius, self.x+self.outerRadius, self.y+self.outerRadius, width=self.width, outline='white')
        
    
#########
    
class ShootingLine():
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.hidden = False
        #self.canvas = canvas
        #self.line = self.canvas.create_rectangle(x - self.x / 2, y - self.y / 2, x + self.x/2, y + self.y /2, fill = "grey")
        #line.pack()

    def setAngle(self, newAngle):
        self.angle = newAngle
    """  
    def incrementAngle(self, dAngle):
        
        if 0.05 <= self.angle <= math.pi-0.05:
            self.angle += dAngle
    """
    def getAngle(self):
        return self.angle
        
    def setStartingPoint(self, x, y):
        self.x = x
        self.y = y
        
    def setHidden(self, hidden):
        self.hidden = hidden
        
    def draw(self, canvas):
        if not self.hidden:
            y2 = HEIGHT
            if self.angle == 0:
                x2 = self.x
                y2 = HEIGHT
            else:
                x2 = y2/math.tan(self.angle)
                x2 += self.x
                y2 = self.y - y2
            canvas.create_line(self.x, self.y, x2, y2, dash=(8, 4))
            
    
   
def insertNewRow(data):
    blockLocations = set(data.blocks.keys())
    
    for r, c in blockLocations:
        block = data.blocks.pop((r, c))
        block.moveDown()        
        if not block.offGrid():
            data.blocks[(r+1, c)] = block

    newPowerUpLocations = set()
    for r, c in data.powerUpLocations:
        r += 1
        if r <= HEIGHT//BLOCKSIZE:
            newPowerUpLocations.add((r, c))
    data.powerUpLocations = newPowerUpLocations
        


    ncols = WIDTH//BLOCKSIZE
    for i in range(ncols//2):
        r = randint(0, ncols-1)
        data.blocks[(0, r)] = Block(0, r, randomBlockNumber(data.levelNum))

    emptyPositionsInFirstRow = []
    for i in range(ncols):
        if (0, i) not in data.blocks:
            emptyPositionsInFirstRow += [i]
    powerUpColumnNumber = choice(emptyPositionsInFirstRow)
    data.powerUpLocations.add((0, powerUpColumnNumber))


def launchBall(data): # will add to the array
    data.launchedBalls.append(Ball(data.launchPosition[0], data.launchPosition[1], data.launchAngle))
    data.remainingBalls -= 1
    data.timeSinceLastLaunch = 0



def prepareForNewLevel(data):
    checkIfGameOver(data)
    data.ballsMoving = False
    data.levelNum += 1
    insertNewRow(data)
    data.nBalls += data.nPowerUps
    data.nPowerUps = 0
    data.remainingBalls = data.nBalls
    data.timeSinceLastLaunch = 0
    data.shootingLine.setStartingPoint(data.launchPosition[0], data.launchPosition[1])

def checkIfGameOver(data):
    for r, c in data.blocks:
        if r == HEIGHT//BLOCKSIZE-1:
            data.gameOver = True

def init(data):
    data.gameOver = False
    data.ballsMoving = False
    data.baselineY = HEIGHT-21 # HEIGHT - (2*radius+1)
    data.launchAngle = math.pi/2
    data.angleIncrement = 0.01
    data.launchAngle = math.pi/2
    data.score = 0
    data.levelNum = 0
    data.blocksize = BLOCKSIZE
    data.nBalls = 1
    data.remainingBalls = 1
    #data.returnedBalls = 0
    data.launchPosition = WIDTH/2, data.baselineY
    data.nPowerUps = 0
    data.timeSinceLastLaunch = 0 # 
    data.timeGap = 50
    data.blocks = {}
    data.powerUpLocations = set()
    data.explosions = set()
    data.launchedBalls = []
    """
    for i in range(30):
        r, c = randint(0, WIDTH//BLOCKSIZE-1), randint(0, HEIGHT//(2 * BLOCKSIZE))
        data.blocks[(r, c)] = Block(r, c, randomBlockNumber(1))
    """
    
    data.shootingLine = ShootingLine(WIDTH/2, HEIGHT-21, data.launchAngle)
    prepareForNewLevel(data)
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if data.gameOver:
        print("game over")
        # to restart the game, put the logic here
    if not data.ballsMoving:
        if event.keysym == "Left":
            data.launchAngle += data.angleIncrement
            data.shootingLine.setAngle(data.launchAngle)
        
        elif event.keysym == "Right":
            data.launchAngle -= data.angleIncrement
            data.shootingLine.setAngle(data.launchAngle)
        elif event.char == " ":
            data.ballsMoving = True
            data.score = data.score + 1

            #data.ball.setAngle(data.shootingLine.getAngle())
            #data.ball.setMoving(True)
            #data.shootingLine.setHidden(True)
            
def timerFired(data): # all the game logic goes here
    
    
    if data.gameOver:
        return

    for explosion in data.explosions.copy(): # because we can't remove while iterating
        if explosion.isOver():
            data.explosions.remove(explosion)


    if not data.ballsMoving:
        return


    data.timeSinceLastLaunch += TIMERDELAY
    if data.remainingBalls > 0 and data.timeSinceLastLaunch >= data.timeGap:
        data.timeSinceLastLaunch = 0
        launchBall(data)


    

    ballsToRemove = len(data.launchedBalls) * [False]
    for i in range(len(data.launchedBalls)):
        ball = data.launchedBalls[i] 
        ball.update(data)
        ballX, ballY = ball.getPosition()

        if ballY == data.baselineY:
            ballsToRemove[i] = True
            

    newLaunchedBalls = []
    for i in range(len(data.launchedBalls)):
        if ballsToRemove[i] == False:
            newLaunchedBalls.append(data.launchedBalls[i])
        else:
            data.launchPosition = data.launchedBalls[i].getPosition() # position of last ball removed can be next play's position

    data.launchedBalls = newLaunchedBalls
    #data.launchedBalls = [data.launchedBalls[i] for i in len(ballsToRemove) if ballsToRemove[i] == False]

    if data.launchedBalls == []:
        if data.remainingBalls == 0:
            prepareForNewLevel(data)
        # prepare for new level


def redrawAll(canvas, data): # only call drawing methods
    if data.gameOver:
        # put code to display game over screen here
        return

    for explosion in data.explosions:
        explosion.draw(canvas)
        
    for gridpos in data.blocks:
        block = data.blocks[gridpos]
        block.draw(canvas, data)

    for gridpos in data.powerUpLocations:
        PowerUp(gridpos[0], gridpos[1]).draw(canvas)
    

    if not data.ballsMoving:
        b = Ball(data.launchPosition[0], data.launchPosition[1], data.launchAngle)
        b.draw(canvas, data)
        data.shootingLine.draw(canvas)
    #data.p.draw(canvas) # for powerup
    else:
        for ball in data.launchedBalls:
            ball.draw(canvas, data)
        

####################################
# use the run function as is
####################################

def run(width=300, height=300):

    def redrawAllWrapper(canvas, data):
        score = 0
        if redrawAllWrapper:
            score =+1
        else:
            pass
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='grey', width=0)
        canvas.create_text(30, 780, text = "Score ="+" "+str(data.score))
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    
    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    
    class Struct(object): pass
    
    data = Struct()
    data.width = width
    data.height = height
    data.score = 0 #<----------
    data.timerDelay = TIMERDELAY # milliseconds
    root = Tk()
    root.wm_title("ballz")
    root.geometry("400x800+500+100")
    data.EXPLOSIONFRAMES = [PhotoImage(file='explosion1.gif',format = 'gif -index %i' %(i)) for i in range(16)]
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    
    
    root.mainloop()  # blocks until window is closed
    

wnd = Tk()
wnd.geometry("2000x1500+300+100")
wnd.config(bg = "black")
wnd.wm_title("ballz")
mainscreen = Main(wnd)
wnd.mainloop()
#run(WIDTH, HEIGHT)

#############################################################################
#References
#https://www.cs.cmu.edu/~rdriley/112/notes/notes-animations-part2.html
#############################################################################