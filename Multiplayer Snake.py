import pygame, sys, random, time
from pygame.locals import *
from pygame.font import *
from random import randint

pygame.init()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKBLUE = (25, 25, 112)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global DISPLAYSURF, FPSCLOCK

    FPSCLOCK = pygame.time.Clock()
    lastTime = pygame.time.get_ticks()
    DISPLAYSURF = pygame.display.set_mode((250, 250), pygame.RESIZABLE)
    pygame.display.set_caption("Growing Snake")
    NUMTILES = 20
    mainBoard = []
    snakeXBlack = []
    snakeYBlack = []
    snakeXWhite = []
    snakeYWhite = []
    for x in range(20):
        column = []
        for y in range(20):
            column.append("E")
        mainBoard.append(column)
    mainBoard[4][9] = "I"
    mainBoard[16][9] = "F"
    mainBoard[10][9] = "A"
    appleX = 10
    appleY = 9
    snakeXBlack.append(16)
    snakeYBlack.append(9)
    snakeXWhite.append(4)
    snakeYWhite.append(9)
    directionBlack = None
    directionWhite = None
    growBlack = False
    growWhite = False
    gameLostBlack = False
    gameLostWhite = False

    while True:
        DISPLAYSURF.fill(DARKBLUE)
        TILEWIDTH = DISPLAYSURF.get_width() / 20
        TILEHEIGHT = DISPLAYSURF.get_width() / 20
        if TILEHEIGHT > 51:
            TILEHEIGHT = 51
            TILEWIDTH = 51
        drawBoard(mainBoard, DISPLAYSURF.get_width(), DISPLAYSURF.get_height(), TILEWIDTH, TILEHEIGHT, gameLostBlack, gameLostWhite)
        width = DISPLAYSURF.get_width()
        height = DISPLAYSURF.get_height()

        currentTime = pygame.time.get_ticks()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == (K_LEFT):
                    if directionBlack != RIGHT:
                        directionBlack = LEFT
                elif event.key == (K_RIGHT):
                    if directionBlack != LEFT:
                        directionBlack = RIGHT
                elif event.key == (K_UP):
                    if directionBlack != DOWN:
                        directionBlack = UP
                elif event.key == (K_DOWN):
                    if directionBlack != UP:
                        directionBlack = DOWN
                elif event.key == (K_a):
                    if directionWhite != RIGHT:
                        directionWhite = LEFT
                elif event.key == (K_d):
                    if directionWhite != LEFT:
                        directionWhite = RIGHT
                elif event.key == (K_w):
                    if directionWhite != DOWN:
                        directionWhite = UP
                elif event.key == (K_s):
                    if directionWhite != UP:
                        directionWhite = DOWN
                elif event.key == K_SPACE and (gameLostBlack or gameLostWhite):
                    for x in range(20):
                        for y in range(20):
                            mainBoard[x][y] = "E"
                    snakeXBlack = []
                    snakeYBlack = []
                    snakeXWhite = []
                    snakeYWhite = []
                    mainBoard[4][9] = "I"
                    mainBoard[16][9] = "F"
                    mainBoard[10][9] = "A"
                    appleX = 10
                    appleY = 9
                    snakeXBlack.append(16)
                    snakeYBlack.append(9)
                    snakeXWhite.append(4)
                    snakeYWhite.append(9)
                    directionBlack = None
                    directionWhite = None
                    grow = False
                    gameLostBlack = False
                    gameLostWhite = False


            if event.type == pygame.VIDEORESIZE:
                old_surface_saved = DISPLAYSURF
                if event.w != width:
                    DISPLAYSURF = pygame.display.set_mode((event.w, event.w), pygame.RESIZABLE)
                if event.h != height:
                    DISPLAYSURF = pygame.display.set_mode((event.h, event.h), pygame.RESIZABLE)
                DISPLAYSURF.blit(old_surface_saved, (0, 0))
                del old_surface_saved

        if currentTime - lastTime >= 100 and directionBlack and directionWhite and not (gameLostBlack or gameLostWhite):
            if directionBlack == UP:
                if snakeYBlack[0] == 0:
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0]][snakeYBlack[0] - 1] == "S" or mainBoard[snakeXBlack[0]][snakeYBlack[0] - 1] == "N":
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0]][snakeYBlack[0] - 1] == "I":
                    gameLostBlack = True
                    gameLostWhite = True
                else:
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "E"
                    originalX = snakeXBlack[0]
                    originalY = snakeYBlack[0]
                    mainBoard[snakeXBlack[0]][snakeYBlack[0] - 1] = "F"
                    if snakeXBlack.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeYBlack[0] = snakeYBlack[0] - 1
                    i = snakeXBlack.__len__() - 1
                    if snakeXBlack.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXBlack[j] = snakeXBlack[j - 1]
                            snakeYBlack[j] = snakeYBlack[j - 1]
                        snakeXBlack[1] = snakeXBlack[0]
                        snakeYBlack[1] = snakeYBlack[0] + 1
            if directionBlack == DOWN:
                if snakeYBlack[0] == 19:
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0]][snakeYBlack[0] + 1] == "S" or mainBoard[snakeXBlack[0]][snakeYBlack[0] + 1] == "N":
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0]][snakeYBlack[0] + 1] == "I":
                    gameLostBlack = True
                    gameLostWhite = True
                else:
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "E"
                    originalX = snakeXBlack[0]
                    originalY = snakeYBlack[0]
                    mainBoard[snakeXBlack[0]][snakeYBlack[0] + 1] = "F"
                    if snakeXBlack.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeYBlack[0] = snakeYBlack[0] + 1
                    i = snakeXBlack.__len__() - 1
                    if snakeXBlack.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXBlack[j] = snakeXBlack[j - 1]
                            snakeYBlack[j] = snakeYBlack[j - 1]
                        snakeXBlack[1] = snakeXBlack[0]
                        snakeYBlack[1] = snakeYBlack[0] - 1
            if directionBlack == LEFT:
                if snakeXBlack[0] == 0:
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0] - 1][snakeYBlack[0]] == "S" or mainBoard[snakeXBlack[0] - 1][snakeYBlack[0]] == "N":
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0] - 1][snakeYBlack[0]] == "I":
                    gameLostBlack = True
                    gameLostWhite = True
                else:
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "E"
                    originalX = snakeXBlack[0]
                    originalY = snakeYBlack[0]
                    mainBoard[snakeXBlack[0] - 1][snakeYBlack[0]] = "F"
                    if snakeXBlack.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeXBlack[0] = snakeXBlack[0] - 1
                    i = snakeXBlack.__len__() - 1
                    if snakeXBlack.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXBlack[j] = snakeXBlack[j - 1]
                            snakeYBlack[j] = snakeYBlack[j - 1]
                        snakeXBlack[1] = snakeXBlack[0] + 1
                        snakeYBlack[1] = snakeYBlack[0]
            if directionBlack == RIGHT:
                if snakeXBlack[0] == 19:
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0] + 1][snakeYBlack[0]] == "S" or mainBoard[snakeXBlack[0] + 1][snakeYBlack[0]] == "N":
                    gameLostBlack = True
                elif mainBoard[snakeXBlack[0] + 1][snakeYBlack[0]] == "I":
                    gameLostBlack = True
                    gameLostWhite = True
                else:
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "E"
                    originalX = snakeXBlack[0]
                    originalY = snakeYBlack[0]
                    mainBoard[snakeXBlack[0] + 1][snakeYBlack[0]] = "F"
                    if snakeXBlack.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeXBlack[0] = snakeXBlack[0] + 1
                    i = snakeXBlack.__len__() - 1
                    if snakeXBlack.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXBlack[j] = snakeXBlack[j - 1]
                            snakeYBlack[j] = snakeYBlack[j - 1]
                        snakeXBlack[1] = snakeXBlack[0] - 1
                        snakeYBlack[1] = snakeYBlack[0]
            if directionWhite == UP:
                if snakeYWhite[0] == 0:
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0]][snakeYWhite[0] - 1] == "N" or mainBoard[snakeXWhite[0]][snakeYWhite[0] - 1] == "S":
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0]][snakeYWhite[0] - 1] == "F":
                    gameLostWhite = True
                    gameLostBlack = True
                else:
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "E"
                    originalX = snakeXWhite[0]
                    originalY = snakeYWhite[0]
                    mainBoard[snakeXWhite[0]][snakeYWhite[0] - 1] = "I"
                    if snakeXWhite.__len__() > 1:
                        mainBoard[originalX][originalY] = "N"
                    snakeYWhite[0] = snakeYWhite[0] - 1
                    i = snakeXWhite.__len__() - 1
                    if snakeXWhite.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXWhite[j] = snakeXWhite[j - 1]
                            snakeYWhite[j] = snakeYWhite[j - 1]
                        snakeXWhite[1] = snakeXWhite[0]
                        snakeYWhite[1] = snakeYWhite[0] + 1
            if directionWhite == DOWN:
                if snakeYWhite[0] == 19:
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0]][snakeYWhite[0] + 1] == "N" or mainBoard[snakeXWhite[0]][snakeYWhite[0] + 1] == "S":
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0]][snakeYWhite[0] + 1] == "F":
                    gameLostWhite = True
                    gameLostBlack = True
                else:
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "E"
                    originalX = snakeXWhite[0]
                    originalY = snakeYWhite[0]
                    mainBoard[snakeXWhite[0]][snakeYWhite[0] + 1] = "I"
                    if snakeXWhite.__len__() > 1:
                        mainBoard[originalX][originalY] = "N"
                    snakeYWhite[0] = snakeYWhite[0] + 1
                    i = snakeXWhite.__len__() - 1
                    if snakeXWhite.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXWhite[j] = snakeXWhite[j - 1]
                            snakeYWhite[j] = snakeYWhite[j - 1]
                        snakeXWhite[1] = snakeXWhite[0]
                        snakeYWhite[1] = snakeYWhite[0] - 1
            if directionWhite == LEFT:
                if snakeXWhite[0] == 0:
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0] - 1][snakeYWhite[0]] == "N" or mainBoard[snakeXWhite[0] - 1][snakeYWhite[0]] == "S":
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0] - 1][snakeYWhite[0]] == "F":
                    gameLostWhite = True
                    gameLostBlack = True
                else:
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "E"
                    originalX = snakeXWhite[0]
                    originalY = snakeYWhite[0]
                    mainBoard[snakeXWhite[0] - 1][snakeYWhite[0]] = "I"
                    if snakeXWhite.__len__() > 1:
                        mainBoard[originalX][originalY] = "N"
                    snakeXWhite[0] = snakeXWhite[0] - 1
                    i = snakeXWhite.__len__() - 1
                    if snakeXWhite.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXWhite[j] = snakeXWhite[j - 1]
                            snakeYWhite[j] = snakeYWhite[j - 1]
                        snakeXWhite[1] = snakeXWhite[0] + 1
                        snakeYWhite[1] = snakeYWhite[0]
            if directionWhite == RIGHT:
                if snakeXWhite[0] == 19:
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0] + 1][snakeYWhite[0]] == "N" or mainBoard[snakeXWhite[0] + 1][snakeYWhite[0]] == "S":
                    gameLostWhite = True
                elif mainBoard[snakeXWhite[0] + 1][snakeYWhite[0]] == "F":
                    gameLostWhite = True
                    gameLostBlack = True
                else:
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "E"
                    originalX = snakeXWhite[0]
                    originalY = snakeYWhite[0]
                    mainBoard[snakeXWhite[0] + 1][snakeYWhite[0]] = "I"
                    if snakeXWhite.__len__() > 1:
                        mainBoard[originalX][originalY] = "N"
                    snakeXWhite[0] = snakeXWhite[0] + 1
                    i = snakeXWhite.__len__() - 1
                    if snakeXWhite.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeXWhite[j] = snakeXWhite[j - 1]
                            snakeYWhite[j] = snakeYWhite[j - 1]
                        snakeXWhite[1] = snakeXWhite[0] - 1
                        snakeYWhite[1] = snakeYWhite[0]
            lastTime = pygame.time.get_ticks()

        if mainBoard[snakeXBlack[0]][snakeYBlack[0]] == mainBoard[appleX][appleY]:
            growBlack = True
            go = True
            while go:
                appleX = randint(0, 19)
                appleY = randint(0, 19)
                if mainBoard[appleX][appleY] != "F" and mainBoard[appleX][appleY] != "S" and mainBoard[appleX][appleY] != "I" and mainBoard[appleX][appleY] != "N":
                    go = False
            mainBoard[appleX][appleY] = "A"

        if mainBoard[snakeXWhite[0]][snakeYWhite[0]] == mainBoard[appleX][appleY]:
            growWhite = True
            go = True
            while go:
                appleX = randint(0, 19)
                appleY = randint(0, 19)
                if mainBoard[appleX][appleY] != "F" and mainBoard[appleX][appleY] != "S" and mainBoard[appleX][appleY] != "I" and mainBoard[appleX][appleY] != "N":
                    go = False
            mainBoard[appleX][appleY] = "A"

        if growBlack:
            posX = snakeXBlack[snakeXBlack.__len__() - 1]
            posY = snakeYBlack[snakeYBlack.__len__() - 1]
            if snakeXBlack.__len__() > 1:
                diffX = snakeXBlack[snakeXBlack.__len__() - 1] - snakeXBlack[snakeXBlack.__len__() - 2]
                diffY = snakeYBlack[snakeYBlack.__len__() - 1] - snakeYBlack[snakeYBlack.__len__() - 2]
                if diffX == 1:
                    snakeXBlack.append(posX + 1)
                    snakeYBlack.append(posY)
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
                elif diffX == -1:
                    snakeXBlack.append(posX - 1)
                    snakeYBlack.append(posY)
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
                elif diffY == 1:
                    snakeXBlack.append(posX)
                    snakeYBlack.append(posY + 1)
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
                elif diffY == -1:
                    snakeXBlack.append(posX)
                    snakeYBlack.append(posY - 1)
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
            else:
                if directionBlack == LEFT:
                    snakeXBlack.append(snakeXBlack[0] + 1)
                    snakeYBlack.append(snakeYBlack[0])
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
                elif directionBlack == RIGHT:
                    snakeXBlack.append(snakeXBlack[0] - 1)
                    snakeYBlack.append(snakeYBlack[0])
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
                elif directionBlack == UP:
                    snakeXBlack.append(snakeXBlack[0])
                    snakeYBlack.append(snakeYBlack[0] + 1)
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
                elif directionBlack == DOWN:
                    snakeXBlack.append(snakeXBlack[0])
                    snakeYBlack.append(snakeYBlack[0] - 1)
                    mainBoard[snakeXBlack[snakeXBlack.__len__() - 1]][snakeYBlack[snakeYBlack.__len__() - 1]] = "S"
            growBlack = False

        if growWhite:
            posX = snakeXWhite[snakeXWhite.__len__() - 1]
            posY = snakeYWhite[snakeYWhite.__len__() - 1]
            if snakeXWhite.__len__() > 1:
                diffX = snakeXWhite[snakeXWhite.__len__() - 1] - snakeXWhite[snakeXWhite.__len__() - 2]
                diffY = snakeYWhite[snakeYWhite.__len__() - 1] - snakeYWhite[snakeYWhite.__len__() - 2]
                if diffX == 1:
                    snakeXWhite.append(posX + 1)
                    snakeYWhite.append(posY)
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
                elif diffX == -1:
                    snakeXWhite.append(posX - 1)
                    snakeYWhite.append(posY)
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
                elif diffY == 1:
                    snakeXWhite.append(posX)
                    snakeYWhite.append(posY + 1)
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
                elif diffY == -1:
                    snakeXWhite.append(posX)
                    snakeYWhite.append(posY - 1)
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
            else:
                if directionWhite == LEFT:
                    snakeXWhite.append(snakeXWhite[0] + 1)
                    snakeYWhite.append(snakeYWhite[0])
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
                elif directionWhite == RIGHT:
                    snakeXWhite.append(snakeXWhite[0] - 1)
                    snakeYWhite.append(snakeYWhite[0])
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
                elif directionWhite == UP:
                    snakeXWhite.append(snakeXWhite[0])
                    snakeYWhite.append(snakeYWhite[0] + 1)
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
                elif directionWhite == DOWN:
                    snakeXWhite.append(snakeXWhite[0])
                    snakeYWhite.append(snakeYWhite[0] - 1)
                    mainBoard[snakeXWhite[snakeXWhite.__len__() - 1]][snakeYWhite[snakeYWhite.__len__() - 1]] = "N"
            growWhite = False

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawBoard(board, width, height, tileWidth, tileHeight, gameLostBlack, gameLostWhite):
    tw = tileWidth
    th = tileHeight
    hSize = (int)(height/th)
    for x in range(19):
        pygame.draw.line(DISPLAYSURF, WHITE, (tw, 0), (tw, height), 1)
        tw += tileWidth
    if th >= 51:
        for y in range(hSize):
            pygame.draw.line(DISPLAYSURF, WHITE, (0, th), (1020, th), 1)
            th += tileHeight
        pygame.draw.line(DISPLAYSURF, WHITE, (1020, 0), (1020, height), 1)
    else:
        for y in range(hSize):
            pygame.draw.line(DISPLAYSURF, WHITE, (0, th), (width, th), 1)
            th += tileHeight
    for x in range(20):
        for y in range(20):
            if board[x][y] == "A":
                appleStartX = x * tileWidth
                appleStartY = y * tileWidth
                pygame.draw.rect(DISPLAYSURF, RED, (appleStartX + tileWidth * 0.25  + 1, appleStartY + tileWidth * 0.25 + 1, tileWidth * 0.5, tileWidth * 0.5), 0)
            if board[x][y] == "F" or board[x][y] == "S":
                dotStartX = x * tileWidth
                dotStartY = y * tileWidth
                pygame.draw.rect(DISPLAYSURF, BLACK, (dotStartX + 1, dotStartY + 1, tileWidth, tileWidth), 0)
            if board[x][y] == "I" or board[x][y] == "N":
                dotStartX = x * tileWidth
                dotStartY = y * tileWidth
                pygame.draw.rect(DISPLAYSURF, WHITE, (dotStartX + 1, dotStartY + 1, tileWidth, tileWidth), 0)
    if gameLostBlack and gameLostWhite:
        fontUsed = pygame.font.Font('freesansbold.ttf', (int)(tileWidth/2))
        pygame.draw.rect(DISPLAYSURF, WHITE, ((int)(width * 0.25), (int)(height * 0.25), (int)(width/2), (int)(height/2)))
        textSurf, textRect = makeText("You Died", BLACK, WHITE, (int)(width * 0.45), (int)(height * 0.4), fontUsed)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfThree, textRectThree = makeText("You ran into each other! No one wins", BLACK, WHITE, (int)(width* 0.29), (int)(height * 0.5), fontUsed)
        DISPLAYSURF.blit(textSurfThree, textRectThree)
        textSurfTwo, textRectTwo = makeText("Press Space To Reset", BLACK, WHITE, (int)(width * 0.38), (int)(height * 0.6), fontUsed)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)
    elif gameLostBlack:
        fontUsed = pygame.font.Font('freesansbold.ttf', (int)(tileWidth / 2))
        pygame.draw.rect(DISPLAYSURF, WHITE, ((int)(width * 0.25), (int)(height * 0.25), (int)(width/2), (int)(height/2)))
        textSurf, textRect = makeText("You Died", BLACK, WHITE, (int)(width * 0.45), (int)(height * 0.4), fontUsed)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfThree, textRectThree = makeText("White snake wins!", BLACK, WHITE, (int)(width * 0.4), (int)(height * 0.5), fontUsed)
        DISPLAYSURF.blit(textSurfThree, textRectThree)
        textSurfTwo, textRectTwo = makeText("Press Space To Reset", BLACK, WHITE, (int)(width * 0.38), (int)(height * 0.6), fontUsed)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)
    elif gameLostWhite:
        fontUsed = pygame.font.Font('freesansbold.ttf', (int)(tileWidth / 2))
        pygame.draw.rect(DISPLAYSURF, WHITE, ((int)(width * 0.25), (int)(height * 0.25), (int)(width/2), (int)(height/2)))
        textSurf, textRect = makeText("You Died", BLACK, WHITE, (int)(width * 0.45), (int)(height * 0.4), fontUsed)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfThree, textRectThree = makeText("Black snake wins!", BLACK, WHITE, (int)(width * 0.4), (int)(height * 0.5), fontUsed)
        DISPLAYSURF.blit(textSurfThree, textRectThree)
        textSurfTwo, textRectTwo = makeText("Press Space To Reset", BLACK, WHITE, (int)(width * 0.38), (int)(height * 0.6), fontUsed)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)

def makeText(text, color, bgcolor, top, left, font):
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

if __name__ == '__main__':
    main()
