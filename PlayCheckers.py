import pygame
from Board.Chessboard import Board
import time
from Board.Tile import Tile
from Pieces.Man import Man
from Pieces.NullPiece import NullPiece
import Logic.logic as logic

pygame.init()
gameDisplay = pygame.display.set_mode((600,600))#((600,680))
pygame.display.set_caption("CheckersChecker")
clock = pygame.time.Clock()

chessboard = Board()
chessboard.createBoard()
chessboard.printBoard()

allTiles = []
allPieces = []
bigVector = []
wewnetrzne = []
##########################
##########################


def ChangePosition(alliance,before,after):
    chessboard.gameTiles[before] = Tile(before, NullPiece())
    chessboard.gameTiles[after] = Tile(after, Man(alliance, after))

def square(x,y,w,h,color):
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])
    allTiles.append([color, [x,y,w,h]])

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
                if not chessboard.gameTiles[number].pieceOnTile.toString() == '-':
                    img = pygame.image.load("./ChessArt/"
                                           + chessboard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                           + chessboard.gameTiles[number].pieceOnTile.toString().upper()
                                           + ".png")
                    img = pygame.transform.scale(img, (75,75))
                    allPieces.append([img, [xpos,ypos], chessboard.gameTiles[number].pieceOnTile])

                xpos += 75

            else:
                square(xpos, ypos, width, hight, black)
                if not chessboard.gameTiles[number].pieceOnTile.toString() == '-':
                    img = pygame.image.load("./ChessArt/"
                                           + chessboard.gameTiles[number].pieceOnTile.alliance[0].upper()
                                           + chessboard.gameTiles[number].pieceOnTile.toString().upper()
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

###MICHAŁOWE TESTY, Prosze nie usuwac###
# chessboard.gameTiles[8] = Tile(8, NullPiece())
# chessboard.gameTiles[10] = Tile(10, Man("White", 10))
# chessboard.gameTiles[12] = Tile(12, NullPiece())
# chessboard.gameTiles[14] = Tile(14, NullPiece())
# chessboard.gameTiles[5] = Tile(5, NullPiece())
# chessboard.gameTiles[5] = Tile(5, NullPiece())
# chessboard.gameTiles[3] = Tile(3, NullPiece())
# drawPieces()
# for x in range(64):
#     chessboard.gameTiles[x] = Tile(x, NullPiece())
# print("\n")
# chessboard.gameTiles[33] = Tile(33, Man("White", 33))
# chessboard.gameTiles[26] = Tile(26, Man("Black", 26))
# chessboard.printBoard()
# print("\n")
# logic.mozliwe_bicia(chessboard,wewnetrzne, bigVector)
# logic.mozliwy_ruch(chessboard,wewnetrzne, bigVector)
# for x in bigVector:
#    # print(x)
#     for tiles in range(64):
#         print('|', end=x[tiles])
#         count += 1
#         if count == 8:
#             print('|', end='\n')
#             count = 0
#     print("\n")


#chessboard.gameTiles[40] = Tile(40, NullPiece())
#chessboard.gameTiles[33] = Tile(33, Man("White", 33))

drawPieces()

message = "All good"
font = pygame.font.SysFont("arial", 30)
text = font.render(message, True, (0, 128, 0))

PointsW = 12
PointsB = 12
wMessage = "W: " + str(PointsW)
textW = font.render(wMessage, True, (0, 128, 0))
bMessage = "B: " + str(PointsB)
textB = font.render(bMessage, True, (0, 128, 0))

quitGame = False
n = 0
while not quitGame:
    if n==0:
        time.sleep(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    gameDisplay.fill((128,128,128))

    gameDisplay.blit(text,
                (300 - text.get_width() // 2, 680 - text.get_height()*1.5))
    gameDisplay.blit(textW,
                     (5, 680 - text.get_height() * 1.5))
    gameDisplay.blit(textB,
                     (600-text.get_width()//1.5, 680 - text.get_height() * 1.5))

    drawPieces()



    if n == 0:
        ChangePosition("White", 44, 37)
    if n != 0:
        ChangePosition("Black", 19, 26)
    n+=1
    for img in allPieces:
        gameDisplay.blit(img[0], img[1])

    pygame.display.update()
    time.sleep(1)
    allTiles = []
    allPieces = []

    clock.tick(60)
