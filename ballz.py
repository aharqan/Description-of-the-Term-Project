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

WIDTH = 400 #the width of the game window
HEIGHT = 800 #the height of the game window
BLOCKSIZE = 40 #size of the blocks (10 in total)
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

# All the shop functionalities will be in this class
class Shop:
    def __init__(self, root):
        self.frame = Frame(root)
        self.root = root
        img1 = ImageTk.PhotoImage(Image.open("Balls1.png"))
        img2 = ImageTk.PhotoImage(Image.open("Themes1.png"))
        img3 = ImageTk.PhotoImage(Image.open("Coins1.png"))
        img20 = ImageTk.PhotoImage(Image.open("Number1.png"))
        canvas1 = Canvas(self.frame, width = 2000, height = 150, bg = "black")
        inner_canvas1 = Canvas(canvas1, width = 300, height = 100, bg = "black")
        canvas1.create_window(50, 30, anchor = NW, window = inner_canvas1)
        inner_canvas1.create_image(110, 65, anchor = CENTER, image = img1)
        inner_canvas1.image = img1
        inner_canvas2 = Canvas(canvas1, width = 300, height = 100, bg = "black")
        inner_canvas4 = Canvas(canvas1, width = 300, height = 100, bg = "black")
        canvas1.create_window(1000, 30, anchor = W, window = inner_canvas2)
        inner_canvas2.create_image(110, 65, anchor = CENTER, image = img3)
        inner_canvas2.image = img3
        inner_canvas15 = Canvas(canvas1, width = 150, height = 50)
        #canvas1.create_window(1000, 130, anchor = W, window = inner_canvas15)
        #inner_canvas15.create_image(10, 30, anchor = W, image = img20)
        #inner_canvas15.image = img20
        #inner_canvas4.create_text(110, 65, anchor = CENTER, text = str(data.nCoins))
        ########################################
        img7 = ImageTk.PhotoImage(Image.open("Ball1().png"))
        img8 = ImageTk.PhotoImage(Image.open("Ball2().png"))
        img9 = ImageTk.PhotoImage(Image.open("Ball3().png"))
        img10 = ImageTk.PhotoImage(Image.open("Ball4().png"))
        img11 = ImageTk.PhotoImage(Image.open("Ball5().png"))
        canvas2 = Canvas(self.frame, width = 2000, height = 250, bg = "grey")
        inner_canvas5 = Canvas(canvas2, width = 200, height = 25, bg = "black")
        inner_canvas6 = Canvas(canvas2, width = 200, height = 25, bg = "black")
        inner_canvas7 = Canvas(canvas2, width = 200, height = 25, bg = "black")
        inner_canvas8 = Canvas(canvas2, width = 200, height = 25, bg = "black")
        inner_canvas9 = Canvas(canvas2, width = 200, height = 25, bg = "black")
        canvas2.create_window(50, 50, anchor = NW, window = inner_canvas5)
        Button1 = Button(inner_canvas5, image = img7)
        inner_canvas5.image = img7
        canvas2.create_window(250, 50, anchor = NW, window = inner_canvas6)
        Button2 = Button(inner_canvas6, image = img8)
        inner_canvas6.image = img8
        canvas2.create_window(450, 50, anchor = NW, window = inner_canvas7)
        Button3 = Button(inner_canvas7, image = img9)
        inner_canvas7.image = img9
        canvas2.create_window(650, 50, anchor = NW, window = inner_canvas8)
        Button4 = Button(inner_canvas8, image = img10)
        inner_canvas8.image = img10
        canvas2.create_window(850, 50, anchor = NW, window = inner_canvas9)
        Button5 = Button(inner_canvas9, image = img11)
        inner_canvas9.image = img11
        Button1.pack(padx = 50, pady = 50)
        Button2.pack(padx = 50, pady = 50)
        Button3.pack(padx = 50, pady = 50)
        Button4.pack(padx = 50, pady = 50)
        Button5.pack(padx = 50, pady = 50)
        ########################################
        canvas3 = Canvas(self.frame, width = 2000, height = 150, bg = "black")
        inner_canvas3 = Canvas(canvas3, width = 300, height = 100, bg = "black")
        canvas3.create_window(50, 30, anchor = NW, window = inner_canvas3)
        inner_canvas3.create_image(90, 65, anchor = CENTER, image = img2)
        inner_canvas3.image = img2
        ########################################
        img4 = ImageTk.PhotoImage(Image.open("Theme3(Blue).png"))
        img5 = ImageTk.PhotoImage(Image.open("Theme2(Yellow).png"))
        img6 = ImageTk.PhotoImage(Image.open("Theme3(Green).png"))
        img12 = ImageTk.PhotoImage(Image.open("Theme2(Blue).png"))
        img13 = ImageTk.PhotoImage(Image.open("Theme3(Orange).png"))
        canvas4 = Canvas(self.frame, width = 2000, height = 250, bg = "grey")
        inner_canvas10 = Canvas(canvas4, width = 200, height = 25, bg = "black")
        inner_canvas11 = Canvas(canvas4, width = 200, height = 25, bg = "black")
        inner_canvas12 = Canvas(canvas4, width = 200, height = 25, bg = "black")
        inner_canvas13 = Canvas(canvas4, width = 200, height = 25, bg = "black")
        inner_canvas14 = Canvas(canvas4, width = 200, height = 25, bg = "black")
        canvas4.create_window(50, 50, anchor = NW, window = inner_canvas10)
        Button1 = Button(inner_canvas10, image = img4)
        inner_canvas10.image = img4
        canvas4.create_window(250, 50, anchor = NW, window = inner_canvas11)
        Button2 = Button(inner_canvas11, image = img5)
        inner_canvas11.image = img5
        canvas4.create_window(450, 50, anchor = NW, window = inner_canvas12)
        Button3 = Button(inner_canvas12, image = img6)
        inner_canvas12.image = img6
        canvas4.create_window(650, 50, anchor = NW, window = inner_canvas13)
        Button4 = Button(inner_canvas13, image = img12)
        inner_canvas13.image = img12
        canvas4.create_window(850, 50, anchor = NW, window = inner_canvas14)
        Button5 = Button(inner_canvas14, image = img13)
        inner_canvas14.image = img13
        Button1.pack(padx = 50, pady = 50)
        Button2.pack(padx = 50, pady = 50)
        Button3.pack(padx = 50, pady = 50)
        Button4.pack(padx = 50, pady = 50)
        Button5.pack(padx = 50, pady = 50)
        canvas1.pack()
        canvas2.pack()
        canvas3.pack()
        canvas4.pack()
        self.frame.pack()
#the animation after the blocks are destroyed
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
            if (row, col) in data.coinsLocations:#########
                data.coinsLocations.remove((row,col))
                data.nCoins.append(int(1))#########
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
        img = ImageTk.PhotoImage(Image.open("Ball1().png"))
        canvas.image = img
        canvas.create_oval(self.x-self.radius+INS, self.y-self.radius+INS, self.x+self.radius-INS, self.y+self.radius-INS, fill = "blue")
'''canvas4.create_window(450, 50, anchor = NW, window = inner_canvas12)
        Button3 = Button(inner_canvas12, image = img6)
        inner_canvas12.image = img6'''
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
    #insert the new row of blocks
    def moveDown(self):
        self.row += 1
    #to draw the collectables off the blocks  
    def offGrid(self):
        return self.row > HEIGHT//BLOCKSIZE
    
    #draw the new balls to collect  
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
        
class Coins:########
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
    #insert the new row of blocks
    def moveDown(self):
        self.row += 1
    #to draw the collectables off the blocks  
    def offGrid(self):
        return self.row > HEIGHT//BLOCKSIZE
    
    #draw the new balls to collect  
    def draw(self, canvas):
        if self.increasing and self.outerRadius >= self.outerMax:
            self.increasing = False
        elif not self.increasing and self.outerRadius <= self.outerMin:
            self.increasing = True
        if self.increasing:
            self.outerRadius += 0.5
        else:
            self.outerRadius -= 0.5
 
        canvas.create_oval(self.x-self.innerRadius, self.y-self.innerRadius, self.x+self.innerRadius, self.y+self.innerRadius, fill='yellow', outline='yellow')
        canvas.create_oval(self.x-self.outerRadius, self.y-self.outerRadius, self.x+self.outerRadius, self.y+self.outerRadius, width=self.width, outline='yellow')
        ###############
#########
#the line where the ball is initialized from  
class ShootingLine():
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.hidden = False
    #
    def setAngle(self, newAngle):
        self.angle = newAngle
    """  
    def incrementAngle(self, dAngle):
        
        if 0.05 <= self.angle <= math.pi-0.05:
            self.angle += dAngle
    """
    def getAngle(self):
        return self.angle
    #where the ball of the last shot stopped, to start the new round  
    def setStartingPoint(self, x, y):
        self.x = x
        self.y = y
    
    def setHidden(self, hidden):
        self.hidden = hidden
    #drawing a line to aim the ball  
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
            
    
#add the new row of the blocks, balls and coins
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

    newCoinsLocations = set()###########
    for r, c in data.coinsLocations:
        r += 1
        if r <= HEIGHT//BLOCKSIZE:
            newCoinsLocations.add((r,c))
    data.coinsLocations = newCoinsLocations###########

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
    for i in range(ncols):##########
        if (0, i) not in data.blocks and (0, i) not in data.powerUpLocations:
            emptyPositionsInFirstRow += [i]
    coinsColumnNumber = choice(emptyPositionsInFirstRow)
    data.coinsLocations.add((0, coinsColumnNumber))###########

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
    #data.nCoins = [] #########
    data.remainingBalls = data.nBalls
    data.timeSinceLastLaunch = 0
    data.shootingLine.setStartingPoint(data.launchPosition[0], data.launchPosition[1])
#check if the blocks reached the shooting line where the game will end
def checkIfGameOver(data):
    for r, c in data.blocks:
        if r == HEIGHT//BLOCKSIZE-1:
            data.gameOver = True
#below will be most of the variable that has the role of a global variable
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
    data.nCoins = [] ########
    data.timeSinceLastLaunch = 0 # 
    data.timeGap = 50
    data.blocks = {}
    data.powerUpLocations = set()
    data.coinsLocations = set() ########
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
        elif event.keysym == "Escape":
            print("hi")
            


            #data.ball.setAngle(data.shootingLine.getAngle())
            #data.ball.setMoving(True)
            #data.shootingLine.setHidden(True)
#the logic of the game goes in the function below     
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
#the main drawing methods will be below
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
    
    for gridpos in data.coinsLocations:###########
        Coins(gridpos[0], gridpos[1]).draw(canvas)



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
#this function runs the main program (Game)
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
        canvas.create_text(35, 780, text = "Score ="+" "+str(data.score))
        canvas.create_text(360, 780, text = "Coins ="+" "+str(sum(data.nCoins)))
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
    data.nCoins = []
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
    
#calling the main window
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