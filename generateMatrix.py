import random


def matrix(mazeBounds: tuple):
    maze = []
    height, width = mazeBounds
    for i in range(0, height + 1):
        temp = []
        for i in range(0, width + 1):
            temp.append(random.choice([0, 1]))
        maze.append(temp)
    maze[0][0] = 1
    end = (height, width)
    maze[end[0]][end[1]] = 1

    return maze, (0, 0), end


