# Updated Animation Starter Code

from tkinter import *
from random import randint, choice

def randomBlockNumber(level):
    return randint(level, 2*level)
    
    



####################################
# customize these functions
####################################

WIDTH = 400
HEIGHT = 800
#main screen
class Main():
    def __init__(self, root):
        self.frame = Frame(root)
        play_button=Button(root, text="Start Game")
        shop_button=Button(root, text="Shop")
        self.frame.pack()
        play_button.pack()
        shop_button.pack()
        
        

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
          
    def draw(self, canvas, data):
        x = data.blocksize * self.col
        y = data.blocksize * self.row
        canvas.create_rectangle(x, y, x + data.blocksize, y + data.blocksize, fill=self.color)
        canvas.create_text(x + 0.5 * data.blocksize, y + 0.5 * data.blocksize, text=str(self.number))
        
        
#all the ball functionalities will be under this class     
class Ball:
    def __init__(self, data):
        self.x = WIDTH/2
        self.y = HEIGHT-100
        self.radius = 8
        self.vx = 10
        self.vy = -10
        self.prevGridCol = self.x // data.blocksize
        self.prevGridRow = self.y // data.blocksize 
        
    def update(self, data):
        self.x += self.vx
        self.y += self.vy
        if self.x <= 0 or self.x >= WIDTH:
            self.vx = -self.vx
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy = -self.vy
        
        # figure out which grid cell we are in
        col = self.x // data.blocksize
        row = self.y // data.blocksize
            
        if (row, col) in data.blocks:
            block = data.blocks[(row, col)]
            block.number -= 1
            if block.number == 0:
                del data.blocks[(row, col)]
            if self.prevGridRow != row: # entered vertically
                self.vy = -self.vy
            if self.prevGridCol != col:
                self.vx = -self.vx
        else:
            self.prevGridRow = row
            self.prevGridCol = col
                
    #To draw the circle  
    def draw(self, canvas, data):
        canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill='white')

class shootingLine():
    def __init__(self, canvas,x, y):
        self.x = 0
        self.y = 750
        self.ball = None
        self.canvas = canvas
        line = self.canvas.create_rectangle(x - self.x / 2, y - self.y / 2, x + self.x/2, y + self.y /2, fill = "grey")
        line.pack()
    



def init(data):
    data.score = 0
    data.blocksize = 40
    data.ball = Ball(data)
    data.blocks = {}
    positions = [(0, 0), (1, 2), (3, 4),(1,1),(2,1),(3,1), (2,2),(0,5),(0,9),(2,8)]
    for r, c in positions:
        data.blocks[(r, c)] = Block(r, c, randomBlockNumber(1))
        
    
    
def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym == "Left":
        print("left")
    elif event.keysym == "Right":
        print("right")

    
def timerFired(data): # all the game logic goes here
    data.ball.update(data)

def redrawAll(canvas, data): # only call drawing methods
    data.ball.draw(canvas, data)
    for gridpos in data.blocks:
        block = data.blocks[gridpos]
        block.draw(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='grey', width=0)
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
    data.timerDelay =  29 # milliseconds
    root = Tk()
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
    

    
run(WIDTH, HEIGHT)

#############################################################################
#References
#layout is from Professor Ryal Riley Class 15112 2018
#############################################################################