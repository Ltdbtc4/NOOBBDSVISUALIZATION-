class node:
    def __init__(self, cords, parent):
        self.cords = cords
        self.Y = self.cords[0]
        self.X = self.cords[1]
        if parent is None:
            self.parent = self
        else:
            self.parent = parent

