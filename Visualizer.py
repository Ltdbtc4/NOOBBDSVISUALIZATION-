import pygame, sys

pygame.init()
clock = pygame.time.Clock()
FPS = 40
black = 0, 0, 0
red = 178, 34, 34
size = width, height = 1000 , 1000
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
green = (0, 255, 0)


def drawMatrix(startingMatrix):
    Ysize = len(startingMatrix)
    Xsize = len(startingMatrix[0])
    blocksize = (width / Xsize, height / Ysize)
    curY = 0
    curX = 0
    for row in startingMatrix:
        curX = 0
        for block in row:
            if block == 1:
                pygame.draw.rect(screen, black, (curX, curY, blocksize[0], blocksize[1]))
                pygame.draw.rect(screen, white, (curX, curY, blocksize[0] -5, blocksize[1] - 5))
            elif block == "PATHWAY":
                pygame.draw.rect(screen, black, (curX, curY, blocksize[0], blocksize[1]))
                pygame.draw.rect(screen, green, (curX, curY, blocksize[0] - 5, blocksize[1] - 5))
            elif block == "BDS":
                pygame.draw.rect(screen, black, (curX, curY, blocksize[0], blocksize[1]))
                pygame.draw.rect(screen, red, (curX, curY, blocksize[0] - 5, blocksize[1] - 5))
            curX += blocksize[0]
        curY += blocksize[1]

def updateMatrix(matrix, cords, newVal):
    # cords passed in as y, x
    if newVal == "PATHWAY":
        matrix[cords[0]][cords[1]] = "PATHWAY"
    elif newVal == "BDS":
        matrix[cords[0]][cords[1]] = "BDS"





def main(shortestPath, startingMatrix, order):
    global FPS
    finished = False
    currentCordsIndex = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if not finished:
            if currentCordsIndex >= len(shortestPath):
                finished = True
                continue
            if len(order) > 0:
                updateMatrix(startingMatrix, order.pop(0), "BDS")
            else:
                FPS = 200
                updateMatrix(startingMatrix, shortestPath[currentCordsIndex], "PATHWAY")
                currentCordsIndex += 1
        screen.fill(black)
        drawMatrix(startingMatrix)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()