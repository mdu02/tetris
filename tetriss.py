## TETRIS.PY
## PLAYS THE GAME TETRIS
## MICHAEL DU
## 2018-06-04

#NOTE: PLEASE RUN THIS GAME AS A PY FILE, IN IDLE YOU NEED TO MANUALLY FOCUS THE GAME WINDOW

#imports
import pygame
from random import randint

#constants (change blocksize for a bigger/smaller screen)
COLS = 10
ROWS = 22
BLOCKSIZE = 30
WIDTH = (COLS * BLOCKSIZE) * 3 / 2
HEIGHT= ROWS * BLOCKSIZE
TICKTIME = 75
pygame.init()

#colours and fonts
GREEN = (  0,200,  0)
BLUE  = (  0,  0,255)
WHITE = (255,255,255)
GREY = (128,128,128)
RED = (255,0,0)
BLACK = (  0,  0,  0)
CYAN = (0,255,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
ORANGE = (255,128,0)
GAMEFONT = pygame.font.SysFont("Arial", BLOCKSIZE * 2 / 3)
GAMEOVERFONT = pygame.font.SysFont("Arial", BLOCKSIZE * 3 / 2)

#block representations; each piece is represented as its four orientations

pieces = [
    #l
    [
    [
    [0,0,0,0],
    [1,1,1,1],
    [0,0,0,0],
    [0,0,0,0]
    ],

    [
    [0,0,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,1,0]
    ],
    
    [
    [0,0,0,0],
    [0,0,0,0],
    [1,1,1,1],
    [0,0,0,0]
    ],
    
    [
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0]
    ]
    ],
    #o
    [
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ]
    ],
    #o
    [
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,2,2,0],
    [0,2,2,0],
    [0,0,0,0]
    ]
    ],
    #T
    [
    [
    [0,0,0,0],
    [0,0,3,0],
    [0,3,3,3],
    [0,0,0,0]
    ],
    [
    [0,3,0,0],
    [0,3,3,0],
    [0,3,0,0],
    [0,0,0,0]
    ],
    [
    [0,3,3,3],
    [0,0,3,0],
    [0,0,0,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,3],
    [0,0,3,3],
    [0,0,0,3],
    [0,0,0,0]
    ]
    ],
     #S
    [
    [
    [0,4,0,0],
    [0,4,4,0],
    [0,0,4,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,0,4,4],
    [0,4,4,0],
    [0,0,0,0]
    ],
    [
    [0,4,0,0],
    [0,4,4,0],
    [0,0,4,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,0,4,4],
    [0,4,4,0],
    [0,0,0,0]
    ]
    ],
    #Z
    [
    [
    [0,0,5,0],
    [0,5,5,0],
    [0,5,0,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,5,5,0],
    [0,0,5,5],
    [0,0,0,0]
    ],
    [
    [0,0,5,0],
    [0,5,5,0],
    [0,5,0,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,5,5,0],
    [0,0,5,5],
    [0,0,0,0]
    ]
    ],
    #J
    [
    [
    [0,0,6,0],
    [0,0,6,0],
    [0,6,6,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,6,0,0],
    [0,6,6,6],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,6,6,0],
    [0,6,0,0],
    [0,6,0,0]
    ],
    [
    [0,0,0,0],
    [6,6,6,0],
    [0,0,6,0],
    [0,0,0,0]
    ]
    ],
    #L
    [
    [
    [0,7,0,0],
    [0,7,0,0],
    [0,7,7,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,7,7,7],
    [0,7,0,0],
    [0,0,0,0]
    ],
    [
    [0,0,0,0],
    [0,7,7,0],
    [0,0,7,0],
    [0,0,7,0]
    ],
    [
    [0,0,0,0],
    [0,0,7,0],
    [7,7,7,0],
    [0,0,0,0]
    ]
    ]
]

#classes

class canvas(object):

    #this class contains a method to draw pieces from a 2d array (blockStore) in different colours 
    def __init__(self, xPos, yPos, xDim, yDim, blockStore):
        self.xPos = xPos
        self.yPos = yPos
        self.xDim = xDim
        self.yDim = yDim
        self.blockStore = blockStore            
    #loops over entire 2d array and for each member, draws it based on its offset from the origin(yPos and xPos) and the size of the blocks(xDim and yDim)
    def draw(self):
        for i in range(self.yDim):
            for j in range(self.xDim):
                #cyan, I
                if self.blockStore[i][j] == 1:
                    pygame.draw.rect(gameWindow, CYAN, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)
                #yellow, O
                if self.blockStore[i][j] == 2:
                    pygame.draw.rect(gameWindow, YELLOW, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)
                #purple, T
                if self.blockStore[i][j] == 3:
                    pygame.draw.rect(gameWindow, PURPLE, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)
                #green, S
                if self.blockStore[i][j] == 4:
                    pygame.draw.rect(gameWindow, GREEN, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)
                #red, Z
                if self.blockStore[i][j] == 5:
                    pygame.draw.rect(gameWindow, RED, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)
                #blue, J
                if self.blockStore[i][j] == 6:
                    pygame.draw.rect(gameWindow, BLUE, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)
                #orange, L
                if self.blockStore[i][j] == 7:
                    pygame.draw.rect(gameWindow, ORANGE, ((self.xPos*BLOCKSIZE)+(j*BLOCKSIZE), (self.yPos*BLOCKSIZE)+(i*BLOCKSIZE), BLOCKSIZE, BLOCKSIZE),0)

#class for game board
class board(canvas):
    def __init__(self, xDim, yDim, blockStore):
        self.xPos = 0
        self.yPos = 0
        self.xDim = xDim
        self.yDim = yDim
        self.blockStore = blockStore
        self.linescleared = 0  
    #clears lines
    def clear(self):
        filled = 0
        rows = []
        #iterates through each row. if said row contains has all 10(or other value) positions filled
        #adds this row to a list of rows to be removed
        for i in range(self.yDim):
            filled = 0
            for j in range(self.xDim):
                if self.blockStore[i][j] != 0:
                    filled += 1
            if filled == COLS:
                rows.append(i)
        #removes row and adds empty row to top to ensure indices remain the same for each row removed
        for i in rows:
            del self.blockStore[i]
            self.blockStore.insert(0, [0]*(COLS+4))
            self.linescleared += 1    
    #if there is a filled position in any of the top two rows, this function returns True
    def gameover(self):
        for i in range(2):
            for j in range(self.xDim):
                if self.blockStore[i][j] != 0:
                    return True
        return False

#class for block
class block(canvas):
    #btype is which block it is, and rotation is which of its four positions it is currently in
    #xpos and ypos determine offset from origin, and xdim and ydim show how big the block is
    def __init__(self):
        self.bType = randint(0,6)
        self.rotation = 0
        self.xPos = (COLS/2) - 2
        self.yPos = 0
        self.xDim = 4
        self.yDim = 4
    #does the same as __init__
    def respawn(self):
        self.bType = randint(0,6)
        self.rotation = 0
        self.xPos = (COLS/2) - 2
        self.yPos = 0
        self.xDim = 4
        self.yDim = 4

    #changes the block stored to reflect new values of bType or rotation
    def block_update(self):
        self.blockStore = pieces[self.bType][self.rotation]

    #checks to see if the block can rotate
    #for each nonzero value of the array(where the block is), checks to see if the block
    #will either be intersecting with the board or offscreen after it has been rotated
    def can_rotate(self, board):
        for i in range(self.yDim):
            for j in range(self.xDim):
                if board.blockStore[i+self.yPos][j+self.xPos] != 0 and pieces[self.bType][(self.rotation + 1)%4][i][j] != 0:
                    return False
                if (i+self.yPos > ROWS - 1 or j+self.xPos < 0 or j+self.xPos > COLS - 1) and pieces[self.bType][(self.rotation + 1)%4][i][j] != 0:
                    return False
        return True

    #rotates the piece by looping through its possible states           
    def cw(self):
        self.rotation += 1
        if self.rotation == 4:
            self.rotation -=4

    #similar to can_rotate, but to see if the piece can drop        
    def canDrop(self, board):
        for i in range(self.yDim):
            for j in range(self.xDim):
                #make sure can't drop off bottom
                if i+self.yPos+1 > ROWS - 1 and self.blockStore[i][j] != 0:
                    return False
                if board.blockStore[i+self.yPos+1][j+self.xPos] != 0 and self.blockStore[i][j] != 0:
                    return False
        return True
    
    #similar to can_rotate, but to see if the piece can go left
    def canLeft(self, board):
        for i in range(self.yDim):
            for j in range(self.xDim):
                #make sure can't go off left
                if j+self.xPos-1 < 0 and self.blockStore[i][j] != 0:
                    return False
                if board.blockStore[i+self.yPos][j+self.xPos-1] != 0 and self.blockStore[i][j] != 0:
                    return False
        return True
    
    #similar to can_rotate, but to see if the piece can go right
    def canRight(self, board):
        for i in range(self.yDim):
            for j in range(self.xDim):
                #make sure can't go off left
                if j+self.xPos+1 > COLS - 1 and self.blockStore[i][j] != 0:
                    return False
                if board.blockStore[i+self.yPos][j+self.xPos+1] != 0 and self.blockStore[i][j] != 0:
                    return False
        return True
    
#redraw function
#draws game boundary, kill line, and renders level and score text
def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.line(gameWindow, WHITE, (COLS * BLOCKSIZE+3, 0),(COLS * BLOCKSIZE+3,HEIGHT),5)
    pygame.draw.line(gameWindow, GREY, (0, BLOCKSIZE*2),(COLS * BLOCKSIZE,BLOCKSIZE*2),5)
    lines1 = GAMEFONT.render("Lines Cleared",1,WHITE)
    lines2 = GAMEFONT.render(str(board.linescleared),1,WHITE)
    level1 = GAMEFONT.render("LEVEL",1,WHITE)
    level2 = GAMEFONT.render(str(level),1,WHITE)
    gameWindow.blit(lines1, (COLS * BLOCKSIZE * 13 / 12 ,(HEIGHT/10)))
    gameWindow.blit(lines2, (COLS * BLOCKSIZE * 5 / 4 ,(HEIGHT*2/10)))
    gameWindow.blit(level1, (COLS * BLOCKSIZE * 7 / 6 ,(HEIGHT*2/5)))
    gameWindow.blit(level2, (COLS * BLOCKSIZE * 5 / 4 ,(HEIGHT/2)))
    
#setup of the board
boardSetup = []
for i in range(ROWS+4):
        boardSetup.append([0]*(COLS+4))
board = board(COLS,ROWS, boardSetup)
currentBlock = block()

#classic tetris music
pygame.mixer.music.load ("Tetris.mp3")  
pygame.mixer.music.queue ("Tetris.mp3")
pygame.mixer.music.play(-1)


#game variables
level = 1

#how often the game forces the piece down
gameSpeed = TICKTIME * 7

#timer
gameTimer = 0

#resets every time an action happens 
lastAction = 0

#intro
print "Welcome to Tetris"
print "Use the left and right arrow keys to move the pieces left and right"
print "Use the up arrow to rotate the pieces clockwise"
print "Use the down arrow to drop the pieces one space"
print "Use the spacebar to drop the pieces as far as they go"
print "Fill up the rows to remove them from the board"
print "The game will get faster the more lines you clear!"
print "If any piece ends up above the grey line, the game will end"

#user confirmation
confirm = raw_input("Type Y and press enter to start the game:  ")
if confirm == 'Y':
    gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
    inPlay = True

#main program
while inPlay: 
    pygame.time.delay(TICKTIME)
    gameTimer += TICKTIME
    redrawGameWindow()
    board.draw()
    currentBlock.block_update()
    currentBlock.draw()
    pygame.display.update()
    board.clear()
    
    #event handling
    #in general, checks the board to see if the action is allowed; if it is, performs it and resets the action timer
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_UP]:
        if currentBlock.can_rotate(board):
            currentBlock.cw()
            lastAction = gameTimer
    if keys[pygame.K_DOWN]:
        if currentBlock.canDrop(board):
            currentBlock.yPos += 1
            lastAction = gameTimer
    if keys[pygame.K_SPACE]:
        while currentBlock.canDrop(board):
            currentBlock.yPos += 1
    if keys[pygame.K_LEFT]:
        if currentBlock.canLeft(board):
            currentBlock.xPos -= 1
            lastAction = gameTimer
    if keys[pygame.K_RIGHT]:
        if currentBlock.canRight(board):
            currentBlock.xPos += 1
            lastAction = gameTimer

    if (gameTimer-lastAction)%gameSpeed == 0 and (gameTimer-lastAction) > 0:
        if currentBlock.canDrop(board):
            currentBlock.yPos += 1
            lastAction = gameTimer

        #checks if the block is completely unable to move. if it is, merges the block into the board and spawns a new block
        elif (currentBlock.canDrop(board) == 0 and currentBlock.canLeft(board) == 0 and currentBlock.canRight(board) == 0):
            for i in range(currentBlock.yDim):
                for j in range(currentBlock.xDim):
                    if currentBlock.blockStore[i][j] != 0:
                        board.blockStore[currentBlock.yPos + i][currentBlock.xPos + j] = currentBlock.blockStore[i][j]

            #if after the block is merged into the board, it is above the kill line, this ends the game
            if board.gameover():
                inPlay = False
            else:
                currentBlock.respawn()
                
        #checks to see if the player has not moved the piece for one "turn". if it is, merges the block into the board and spawns a new block
        else:
            for i in range(currentBlock.yDim):
                for j in range(currentBlock.xDim):
                    if currentBlock.blockStore[i][j] != 0:
                            board.blockStore[currentBlock.yPos + i][currentBlock.xPos + j] = currentBlock.blockStore[i][j]
            if board.gameover():
                inPlay = False
            else:
                currentBlock.respawn()
                
    #level handling; speeds up the more lines are cleared
    if board.linescleared >= 25:
        gameSpeed = TICKTIME * 2
        level = 6
    elif board.linescleared >= 20:
        gameSpeed = TICKTIME * 3
        level = 5
    elif board.linescleared >= 15:
        gameSpeed = TICKTIME * 4
        level = 4
    elif board.linescleared >= 10:
        gameSpeed = TICKTIME * 5
        level = 3
    elif board.linescleared >= 5:
        gameSpeed = TICKTIME * 6
        level = 2
        
#game over screen
gameWindow.fill(BLACK)
gameOver1 = GAMEOVERFONT.render("GAME OVER",1,WHITE)
gameOver2 = GAMEFONT.render("You cleared " + str(board.linescleared) + " lines and got to level " + str(level),1,WHITE)
gameWindow.blit(gameOver1, (COLS * BLOCKSIZE * 2/5 ,(HEIGHT * 2/5)))
gameWindow.blit(gameOver2, (COLS * BLOCKSIZE/3 ,(HEIGHT* 3/5)))
pygame.display.update()
pygame.time.delay(5000)

#end
pygame.quit()
