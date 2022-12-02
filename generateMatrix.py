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
    maze[-1][-1] = 1
    return maze, (0, 0), (-1, -1)


from queue import LifoQueue
from PIL import Image
import numpy as np
from random import choice


def generate_maze(width, height):
    maze = Image.new('RGB', (2 * width + 1, 2 * height + 1), 'black')
    pixels = maze.load()

    # Create a path on the very top and bottom so that it has an entrance/exit
    pixels[1, 0] = (255, 255, 255)
    pixels[-2, -1] = (255, 255, 255)

    stack = LifoQueue()
    cells = np.zeros((width, height))
    cells[0, 0] = 1
    stack.put((0, 0))

    while not stack.empty():
        x, y = stack.get()

        adjacents = []
        if x > 0 and cells[x - 1, y] == 0:
            adjacents.append((x - 1, y))
        if x < width - 1 and cells[x + 1, y] == 0:
            adjacents.append((x + 1, y))
        if y > 0 and cells[x, y - 1] == 0:
            adjacents.append((x, y - 1))
        if y < height - 1 and cells[x, y + 1] == 0:
            adjacents.append((x, y + 1))

        if adjacents:
            stack.put((x, y))

            neighbour = choice(adjacents)
            neighbour_on_img = (neighbour[0] * 2 + 1, neighbour[1] * 2 + 1)
            current_on_img = (x * 2 + 1, y * 2 + 1)
            wall_to_remove = (neighbour[0] + x + 1, neighbour[1] + y + 1)

            pixels[neighbour_on_img] = (255, 255, 255)
            pixels[current_on_img] = (255, 255, 255)
            pixels[wall_to_remove] = (255, 255, 255)

            cells[neighbour] = 1
            stack.put(neighbour)

    return maze


def generateM(w, h) -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("width", nargs="?", type=int, default=32)
    parser.add_argument("height", nargs="?", type=int, default=None)
    parser.add_argument('--output', '-o', nargs='?', type=str, default='generated_maze.png')
    args = parser.parse_args()

    size = (w, h)

    maze = generate_maze(*size)
    maze.save(args.output)


def generate2D():
    normalArr = []
    x = Image.open("generated_maze.png")
    data = np.asarray(x)
    temp = []
    for row in data:
        temp = []
        for px in row:
            if px[0] == 255:
                temp.append(1)
            else:
                temp.append(0)
        normalArr.append(temp)
    return normalArr


def jet(w, h):
    generate_maze(w, h)
    generateM(w, h)
    ms =  generate2D()
    # for row in ms:
    #     print(row)
    ms[0][0] = 1
    ms[-1][-1] = 1
    return ms, (0, 0), (-1, -1)



