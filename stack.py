class stack:
    def __init__(self):
        self.self = []

    def push(self, element):
        self.self.append(element)

    def pop(self):
        # pop 0 for BFS pop -1 for DFS
        return self.self.pop(0)

    def __len__(self):
        return len(self.self)

