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

UP = 'up"'
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
    snakeX = []
    snakeY = []
    for x in range(20):
        column = []
        for y in range(20):
            column.append("E")
        mainBoard.append(column)
    mainBoard[4][9] = "A"
    mainBoard[16][9] = "F"
    appleX = 4
    appleY = 9
    snakeX.append(16)
    snakeY.append(9)
    direction = None
    grow = False
    gameLost = False

    while True:
        DISPLAYSURF.fill(DARKBLUE)
        TILEWIDTH = DISPLAYSURF.get_width() / 20
        TILEHEIGHT = DISPLAYSURF.get_width() / 20
        if TILEHEIGHT > 51:
            TILEHEIGHT = 51
            TILEWIDTH = 51
        drawBoard(mainBoard, DISPLAYSURF.get_width(), DISPLAYSURF.get_height(), TILEWIDTH, TILEHEIGHT, gameLost)
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
                elif event.key in (K_LEFT, K_a):
                    if direction != RIGHT:
                        direction = LEFT
                elif event.key in (K_RIGHT, K_d):
                    if direction != LEFT:
                        direction = RIGHT
                elif event.key in (K_UP, K_w):
                    if direction != DOWN:
                        direction = UP
                elif event.key in (K_DOWN, K_s):
                    if direction != UP:
                        direction = DOWN
                elif event.key == K_SPACE and gameLost:
                    for x in range(20):
                        for y in range(20):
                            mainBoard[x][y] = "E"
                    snakeX = []
                    snakeY = []
                    mainBoard[4][9] = "A"
                    mainBoard[16][9] = "F"
                    appleX = 4
                    appleY = 9
                    snakeX.append(16)
                    snakeY.append(9)
                    direction = None
                    grow = False
                    gameLost = False


            if event.type == pygame.VIDEORESIZE:
                old_surface_saved = DISPLAYSURF
                if event.w != width:
                    DISPLAYSURF = pygame.display.set_mode((event.w, event.w), pygame.RESIZABLE)
                if event.h != height:
                    DISPLAYSURF = pygame.display.set_mode((event.h, event.h), pygame.RESIZABLE)
                DISPLAYSURF.blit(old_surface_saved, (0, 0))
                del old_surface_saved

        if currentTime - lastTime >= 100 and direction and not gameLost:
            if direction == UP:
                if snakeY[0] == 0:
                    gameLost = True
                elif mainBoard[snakeX[0]][snakeY[0] - 1] == "S":
                    gameLost = True
                else:
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "E"
                    originalX = snakeX[0]
                    originalY = snakeY[0]
                    mainBoard[snakeX[0]][snakeY[0] - 1] = "F"
                    if snakeX.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeY[0] = snakeY[0] - 1
                    i = snakeX.__len__() - 1
                    if snakeX.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeX[j] = snakeX[j - 1]
                            snakeY[j] = snakeY[j - 1]
                        snakeX[1] = snakeX[0]
                        snakeY[1] = snakeY[0] + 1
            elif direction == DOWN:
                if snakeY[0] == 19:
                    gameLost = True
                elif mainBoard[snakeX[0]][snakeY[0] + 1] == "S":
                    gameLost = True
                else:
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "E"
                    originalX = snakeX[0]
                    originalY = snakeY[0]
                    mainBoard[snakeX[0]][snakeY[0] + 1] = "F"
                    if snakeX.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeY[0] = snakeY[0] + 1
                    i = snakeX.__len__() - 1
                    if snakeX.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeX[j] = snakeX[j - 1]
                            snakeY[j] = snakeY[j - 1]
                        snakeX[1] = snakeX[0]
                        snakeY[1] = snakeY[0] - 1
            elif direction == LEFT:
                if snakeX[0] == 0:
                    gameLost = True
                elif mainBoard[snakeX[0] - 1][snakeY[0]] == "S":
                    gameLost = True
                else:
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "E"
                    originalX = snakeX[0]
                    originalY = snakeY[0]
                    mainBoard[snakeX[0] - 1][snakeY[0]] = "F"
                    if snakeX.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeX[0] = snakeX[0] - 1
                    i = snakeX.__len__() - 1
                    if snakeX.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeX[j] = snakeX[j - 1]
                            snakeY[j] = snakeY[j - 1]
                        snakeX[1] = snakeX[0] + 1
                        snakeY[1] = snakeY[0]
            elif direction == RIGHT:
                if snakeX[0] == 19:
                    gameLost = True
                elif mainBoard[snakeX[0] + 1][snakeY[0]] == "S":
                    gameLost = True
                else:
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "E"
                    originalX = snakeX[0]
                    originalY = snakeY[0]
                    mainBoard[snakeX[0] + 1][snakeY[0]] = "F"
                    if snakeX.__len__() > 1:
                        mainBoard[originalX][originalY] = "S"
                    snakeX[0] = snakeX[0] + 1
                    i = snakeX.__len__() - 1
                    if snakeX.__len__() > 1:
                        for x in range(i):
                            j = i - x
                            snakeX[j] = snakeX[j - 1]
                            snakeY[j] = snakeY[j - 1]
                        snakeX[1] = snakeX[0] - 1
                        snakeY[1] = snakeY[0]
            lastTime = pygame.time.get_ticks()

        if mainBoard[snakeX[0]][snakeY[0]] == mainBoard[appleX][appleY]:
            grow = True
            go = True
            while go:
                appleX = randint(0, 19)
                appleY = randint(0, 19)
                if mainBoard[appleX][appleY] != "F" and mainBoard[appleX][appleY] != "S":
                    go = False
            mainBoard[appleX][appleY] = "A"

        if grow:
            posX = snakeX[snakeX.__len__() - 1]
            posY = snakeY[snakeY.__len__() - 1]
            if snakeX.__len__() > 1:
                diffX = snakeX[snakeX.__len__() - 1] - snakeX[snakeX.__len__() - 2]
                diffY = snakeY[snakeY.__len__() - 1] - snakeY[snakeY.__len__() - 2]
                if diffX == 1:
                    snakeX.append(posX + 1)
                    snakeY.append(posY)
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
                elif diffX == -1:
                    snakeX.append(posX - 1)
                    snakeY.append(posY)
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
                elif diffY == 1:
                    snakeX.append(posX)
                    snakeY.append(posY + 1)
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
                elif diffY == -1:
                    snakeX.append(posX)
                    snakeY.append(posY - 1)
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
            else:
                if direction == LEFT:
                    snakeX.append(snakeX[0] + 1)
                    snakeY.append(snakeY[0])
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
                elif direction == RIGHT:
                    snakeX.append(snakeX[0] - 1)
                    snakeY.append(snakeY[0])
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
                elif direction == UP:
                    snakeX.append(snakeX[0])
                    snakeY.append(snakeY[0] + 1)
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
                elif direction == DOWN:
                    snakeX.append(snakeX[0])
                    snakeY.append(snakeY[0] - 1)
                    mainBoard[snakeX[snakeX.__len__() - 1]][snakeY[snakeY.__len__() - 1]] = "S"
            grow = False

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawBoard(board, width, height, tileWidth, tileHeight, gameLost):
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
    if gameLost:
        fontUsed = pygame.font.Font('freesansbold.ttf', (int)(tileWidth/2))
        pygame.draw.rect(DISPLAYSURF, WHITE, ((int)(width * 0.25), (int)(height * 0.25), (int)(width/2), (int)(height/2)))
        textSurf, textRect = makeText("You Died", BLACK, WHITE, (int)(width * 0.45), (int)(height * 0.4), fontUsed)
        DISPLAYSURF.blit(textSurf, textRect)
        textSurfTwo, textRectTwo = makeText("Press Space To Reset", BLACK, WHITE, (int)(width * 0.38), (int)(height * 0.6), fontUsed)
        DISPLAYSURF.blit(textSurfTwo, textRectTwo)

def makeText(text, color, bgcolor, top, left, font):
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

if __name__ == '__main__':
    main()
