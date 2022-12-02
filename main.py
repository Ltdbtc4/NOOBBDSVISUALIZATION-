import Visualizer
import generateMatrix
from node import node
from stack import stack

startingMatrix = [[1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
                  [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
                  [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
                  [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                  [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                  [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
                  [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
                  [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
                  [1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
                  [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                  [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1],
                  [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                  [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1],
                  [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
                  [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                  [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
                  [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
                  [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
                  [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                  [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                  [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]


# startingMatrix = [[1, 1, 1, 1],
#                   [0, 1, 1, 0],
#                   [0, 1, 1, 1]]

# goal is to use DFS to get from (0, 0) to (0, 2) in the shortest amount of time. There are 2 valid paths from start
# to finish with a lengths of 3 and 6 respectively.

# first goal would be to convert maze into tree
# called findNeighbours which finds and returns all neighbours other than the nodes parent will abstract away once done
# NODE MUST ONLY CONTAIN DISTINCT NEIGHBOURS

def findNeighbours(MATRIX, NODE):
    NEIGHBOURS = []
    # need to find all left, right, top, bottom neighbours excluding parents
    # checks if you can find left neighbour within maze bounds
    if NODE.X > 0:
        NEIGHBOURS.append(node((NODE.Y, NODE.X - 1), NODE))
    # checks if you can find right neighbour within maze bounds
    if NODE.X < len(MATRIX[NODE.Y]) - 1:
        NEIGHBOURS.append(node((NODE.Y, NODE.X + 1), NODE))
    # checks if you can find top neighbour within maze bounds
    if NODE.Y > 0:
        NEIGHBOURS.append(node((NODE.Y - 1, NODE.X), NODE))
    # checks if you can find bottom neighbour within maze bounds
    if NODE.Y < len(MATRIX) - 1:
        NEIGHBOURS.append(node((NODE.Y + 1, NODE.X), NODE))
    # filters all neighbour's by removing invalid neighbours; parents and walls
    validNeighbours = []
    for neighbour in NEIGHBOURS:
        # deletes parent
        if neighbour.cords == NODE.parent.cords:
            continue
        # deletes all invalid nodes
        if MATRIX[neighbour.Y][neighbour.X] == 0:
            continue
        validNeighbours.append(neighbour)
    return validNeighbours


# will check if a node path only contains distinct nodes in order to ensure that a sequence does not repeat as
# children can have 2 parents
def pathIsDistinct(NODE):
    finished = False
    cords = []
    curNode = NODE
    while not finished:
        # this will check if the current node is the first node as the first nodes starting node is self
        if curNode.parent == curNode:
            return True
        # checks if the cords of a current node parent have already been seen
        if curNode.parent.cords in cords:
            return False
        # adds parent cords to cord and sets new node as parent
        cords.append(curNode.parent.cords)
        curNode = curNode.parent


def tracePath(NODE):
    finished = False
    pathCords = []
    curNode = NODE
    while not finished:
        # this will check if the current node is the first node as the first nodes starting node is self
        if curNode.parent == curNode:
            pathCords.append(curNode.cords)
            return pathCords
        pathCords.append(curNode.cords)
        curNode = curNode.parent
    return pathCords


def breadthDepthSearch(MATRIX, startCords, endCords):
    # creates a list called routes to keep track of all current successful paths
    routes = []
    # initializes stack and populates with starting node
    order = []
    Stack = stack()
    Stack.push(node(startCords, None))
    while len(Stack) > 0:
        # pops a node from the stack
        currentNode = Stack.pop()
        if currentNode.cords not in order:
            order.append(currentNode.cords)
        # checks if distinct to stop repetition
        if not pathIsDistinct(currentNode):
            continue
        # checks if reached endCords
        if currentNode.cords == endCords:
            routes.append(tracePath(currentNode))
        # finds neighbour's
        neighbours = findNeighbours(MATRIX, currentNode)
        # pushes neighbour's into stack
        for neighbour in neighbours:
            Stack.push(neighbour)
    return routes, order


def getShortestPath(matrix):
    # ignore unoptimized spaghetti mess
    sizes = {}
    for i, m in enumerate(matrix):
        sizes[i] = len(m)
    curLow = 1000000
    ind = 0
    for key in sizes:
        if sizes[key] < curLow:
            curLow = sizes[key]
            ind = key
    return ind


def getShortest():
    # global startingMatrix
    # start = (0, 0)
    # end = (29, 29)
    while True:
        startingMatrix, start, end = generateMatrix.matrix((10, 10))
        result, order = breadthDepthSearch(startingMatrix, start, end)
        if len(result) > 0:
            shortestPath = result[getShortestPath(result)]
            return shortestPath, startingMatrix, order


if __name__ == "__main__":
    sp, sm, order = getShortest()
    Visualizer.main(sp, sm, order)
