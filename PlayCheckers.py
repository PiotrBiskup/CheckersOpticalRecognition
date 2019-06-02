import pygame
from Board.Chessboard import Board
import time
from Board.Tile import Tile
from Pieces.Man import Man
from Pieces.King import King
from Pieces.NullPiece import NullPiece
import Logic.logic as logic

pygame.init()
gameDisplay = pygame.display.set_mode((600,680))#((600,680))
pygame.display.set_caption("CheckersChecker")
clock = pygame.time.Clock()

chessboard = Board()
chessboard.createBoard()
# chessboard.printBoard()

allTiles = []
allPieces = []
currentTiles = []
# for x in range(64):
#     currentTiles.append(Tile(x,NullPiece()))
# for gameTile in currentTiles:
#     if (gameTile.tileCoordinate % 2 == 1 and gameTile.tileCoordinate < 8):
#         currentTiles[gameTile.tileCoordinate] = Tile(gameTile.tileCoordinate, Man("Black", gameTile.tileCoordinate))
#     if (gameTile.tileCoordinate % 2 == 0 and gameTile.tileCoordinate >= 8 and gameTile.tileCoordinate < 16):
#         currentTiles[gameTile.tileCoordinate] = Tile(gameTile.tileCoordinate, Man("Black", gameTile.tileCoordinate))
#     if (gameTile.tileCoordinate % 2 == 1 and gameTile.tileCoordinate >= 16 and gameTile.tileCoordinate < 25):
#         currentTiles[gameTile.tileCoordinate] = Tile(gameTile.tileCoordinate, Man("Black", gameTile.tileCoordinate))
#
# for gameTile in currentTiles:
#     if (gameTile.tileCoordinate%2==0 and gameTile.tileCoordinate>39 and gameTile.tileCoordinate<48):
#         currentTiles[gameTile.tileCoordinate] = Tile(gameTile.tileCoordinate, Man("White",gameTile.tileCoordinate))
#     if (gameTile.tileCoordinate%2==1 and gameTile.tileCoordinate>=48 and gameTile.tileCoordinate<56):
#         currentTiles[gameTile.tileCoordinate] = Tile(gameTile.tileCoordinate, Man("White",gameTile.tileCoordinate))
#     if (gameTile.tileCoordinate%2==0 and gameTile.tileCoordinate>=56 and gameTile.tileCoordinate<64):
#         currentTiles[gameTile.tileCoordinate] = Tile(gameTile.tileCoordinate, Man("White",gameTile.tileCoordinate))
# currentTiles[0] = Tile(0, Man("Black", 0))
# currentTiles[1] = Tile(1, NullPiece())

currentTiles = ['n', 'n', 'n', 'BM', 'n', 'BM', 'n', 'BM', 'BM', 'n', 'BM', 'n', 'BM', 'n', 'BM', 'n', 'n', 'BM', 'n', 'BM', 'n', 'n', 'n', 'BM', 'n', 'n', 'n', 'n', 'n', 'n', 'BM', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'WM', 'n', 'WM', 'n', 'WM', 'n', 'WM', 'n','n', 'WM', 'n', 'WM', 'n', 'WM', 'n', 'WM', 'WM', 'n', 'WM', 'n', 'WM', 'n', 'WM', 'n']
lastMove = "Black"
correct = True
##########################
##########################


def ChangePosition(alliance,before,after):
    chessboard.gameTiles[before] = Tile(before, NullPiece())
    chessboard.gameTiles[after] = Tile(after, Man(alliance, after))

def square(x,y,w,h,color):
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])
    allTiles.append([color, [x,y,w,h]])

def GoBack(currentTiles):
    n = 0
    for gameTile in currentTiles:
        n += 1
        if (gameTile != chessboard.gameTiles[n].toString()):
            correct = False
            break
        if (gameTile == chessboard.gameTiles[n].toString() and n == 63):
            correct = True

#please check...
def newBoard(lastMove):
    n=0
    for gameTile in currentTiles:
        n+=1
        if(gameTile == 'n'):
            chessboard.gameTiles[n] = Tile(n, NullPiece())
        if (gameTile == 'BM'):
            chessboard.gameTiles[n] = Tile(n, Man("Black",n))
        if (gameTile == 'BK'):
            chessboard.gameTiles[n] = Tile(n, King("Black",n))
        if (gameTile == 'WM'):
            chessboard.gameTiles[n] = Tile(n, Man("White",n))
        if (gameTile == 'WK'):
            chessboard.gameTiles[n] = Tile(n, King("White",n))
    if (lastMove == "Black"):
        lastMove = "White"
    if (lastMove == "White"):
        lastMove = "Black"

#need to check that...
def SeeMove(currentTiles):
        see = logic.Compare(chessboard,bigVector)
        if (see == True):
            correct == True
            newBoard(lastMove)
        #temp # need to add notifications
        if (see == False):
            correct == False
            #notification


def drawPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 75
    hight = 75
    black = (0,0,0)
    white = (255,255,255)
    number = 0

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                square(xpos, ypos, width, hight, white)
                if not chessboard.gameTiles[number].pieceOnTile.toString() == 'n':
                    img = pygame.image.load("./ChessArt/"
                                           #+ chessboard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                           + chessboard.gameTiles[number].pieceOnTile.toString()
                                           + ".png")
                    img = pygame.transform.scale(img, (75,75))
                    allPieces.append([img, [xpos,ypos], chessboard.gameTiles[number].pieceOnTile])

                xpos += 75

            else:
                square(xpos, ypos, width, hight, black)
                if not chessboard.gameTiles[number].pieceOnTile.toString() == 'n':
                    img = pygame.image.load("./ChessArt/"
                                           #+ chessboard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                           + chessboard.gameTiles[number].pieceOnTile.toString()
                                           + ".png")
                    img = pygame.transform.scale(img, (75, 75))
                    allPieces.append([img, [xpos, ypos], chessboard.gameTiles[number].pieceOnTile])

                xpos += 75

            color += 1
            number += 1

        color += 1
        xpos = 0
        ypos += 75


##########################
##########################


drawPieces()

for img in allPieces:
    gameDisplay.blit(img[0], img[1])
pygame.display.update()
time.sleep(2)
allTiles = []
allPieces = []
count=0
wewnetrzne=[]
bigVector=[]

###MICHAŁOWE TESTY, Prosze nie usuwac###
# chessboard.gameTiles[8] = Tile(8, NullPiece())
# chessboard.gameTiles[10] = Tile(10, Man("White", 10))
# chessboard.gameTiles[12] = Tile(12, NullPiece())
# chessboard.gameTiles[14] = Tile(14, NullPiece())
# chessboard.gameTiles[5] = Tile(5, NullPiece())
# chessboard.gameTiles[5] = Tile(5, NullPiece())
# chessboard.gameTiles[3] = Tile(3, NullPiece())
drawPieces()
for x in range(64):
    chessboard.gameTiles[x] = Tile(x, NullPiece())
print("\n")
# chessboard.gameTiles[8] = Tile(8, King("Black", 8))
# # chessboard.gameTiles[56] = Tile(56, King("Black", 56))

#chessboard.gameTiles[44] = Tile(44, King("Black", 44))
#chessboard.gameTiles[35] = Tile(35, King("White", 35))
#chessboard.gameTiles[17] = Tile(17, King("White", 17))
#chessboard.gameTiles[24] = Tile(24, King("White", 24))
#chessboard.gameTiles[37] = Tile(37, King("White", 37))
# chessboard.gameTiles[19] = Tile(19, Man("White", 19))
# chessboard.gameTiles[35] = Tile(35, Man("White", 35))
# chessboard.gameTiles[8] = Tile(8, Man("Black", 8))
# chessboard.gameTiles[33] = Tile(33, Man("White", 33))
chessboard.gameTiles[26] = Tile(26, Man("White", 26))
#chessboard.gameTiles[44] = Tile(44, Man("White", 4))
chessboard.gameTiles[17] = Tile(17, Man("Black", 17))
# chessboard.printBoard()
print("\n")
ruchy = []
bicia =[]
wielokrotne =[]
logic.Generator_bialych(chessboard,ruchy,bicia,wielokrotne)
logic.Generator_czarnych(chessboard,ruchy,bicia,wielokrotne)
chessboard.gameTiles[17] = Tile(17, NullPiece())
chessboard.gameTiles[26] = Tile(26, NullPiece())
chessboard.gameTiles[35] = Tile(35, Man("Black", 35))
print(logic.Komunikaty(chessboard,ruchy,bicia,wielokrotne))

# for x in ruchy:
#     print('', '\n')
#     for idx, tiles in enumerate(x):
#         print('|', end=x[idx])
#         count += 1
#         if count == 8:
#             print('|', end='\n')
#             count = 0
#     print("\n")

def points():
    PointsW=0
    PointsB=0
    for tile in chessboard.gameTiles:
        if chessboard.gameTiles[tile].pieceOnTile.toString()[0] == 'B':
            PointsB+=1
        if chessboard.gameTiles[tile].pieceOnTile.toString()[0] == 'W':
            PointsW+=1
    return PointsB, PointsW

#chessboard.gameTiles[40] = Tile(40, NullPiece())
#chessboard.gameTiles[33] = Tile(33, Man("White", 33))

# drawPieces()

message = "All good"
font = pygame.font.SysFont("arial", 30)
text = font.render(message, True, (0, 128, 0))

global PointsW
PointsW = 12
global PointsB
PointsB = 12
wMessage = "W: " + str(PointsW)
textW = font.render(wMessage, True, (0, 128, 0))
bMessage = "B: " + str(PointsB)
textB = font.render(bMessage, True, (0, 128, 0))

quitGame = False
n = 0
while not quitGame:
    # if n==0:
    #     time.sleep(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    gameDisplay.fill((128,128,128))

    PointsB, PointsW = points()

    wMessage = "W: " + str(PointsW)
    textW = font.render(wMessage, True, (0, 128, 0))
    bMessage = "B: " + str(PointsB)
    textB = font.render(bMessage, True, (0, 128, 0))

    gameDisplay.blit(text,
                (300 - text.get_width() // 2, 680 - text.get_height()*1.5))
    gameDisplay.blit(textW,
                     (5, 680 - text.get_height() * 1.5))
    gameDisplay.blit(textB,
                     (600-text.get_width()//1.5, 680 - text.get_height() * 1.5))

    drawPieces()



    # if n == 0:
    #     ChangePosition("White", 44, 37)
    # if n != 0:
    #     ChangePosition("Black", 19, 26)
    # n+=1
    for img in allPieces:
        gameDisplay.blit(img[0], img[1])

    pygame.display.update()
    time.sleep(1)

    if (correct == True):
        SeeMove(currentTiles)
    if (correct == False):
        GoBack(currentTiles)


    allTiles = []
    allPieces = []

    clock.tick(60)
