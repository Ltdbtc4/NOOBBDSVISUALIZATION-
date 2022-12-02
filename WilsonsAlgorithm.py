import random

class cell:
    def __init__(self, cords: tuple, matrix: array, state: int):
        self.cords = cords
        self.matrix = matrix
        self.state = state
        self.x = x
        self.y = y
        self.neighbours = []
        self.updateNeighbours()

    def updateNeighbours(self):
        self.neighbours = []
        # check left right top and bottom for valid neighbours
        if y > 0:
            self.neighbours.append(cell((y + 1, x), self.matrix))
        if y > len(self.matrix) - 1:
            self.neighbours.append(cell((y - 1, x), self.matrix))
        if x > 0:
            self.neighbours.append(cell((y, x - 1), self.matrix))
        if x < len(self.matrix[y]) -1:
            self.neighbours.append(cell((y, x + 1), self.matrix))
        # filter neighbours



def genMatrix(ySize, xSize):
    #ySize matrix height
    #xSize matrix length
    # n * n matrix
    matrix = []
    matrix = [xSize * [cell((0, 1), matrix, 0] for i in range(ySize)]
    # choose random point in maze to initialize

    finished = True
    START =  cell((random.randint(0, ySize), random.randint(0, xSize)), matrix, 1)
    START = 1



def chooseRandomNeighbour(matrix, cell)




print(genMatrix(10, 10))