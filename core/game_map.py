from math import floor
from utils.handler.logging import Logger
from utils.check import between
from typing import Tuple

class GameMap():
    def __init__(
        self, 
        size: int, 
        startPoint:Tuple[int, int]
        ):
        self.size = size
        self.table = [[0 for _ in range(size)] for _ in range(size)]
        self._startPoint = startPoint if between(startPoint[0], 0, size) and between(startPoint[1], 0, size) else (floor(size/2), floor(size/2))

    def action(self):
        # print([i for i in range(self.size)])
        for i in range(self.size):
            # print(i, end="")
            # print(self.table[i])
            for j in range(self.size):
                if self.table[i][j] <= 0:
                    continue
                self.table[i][j]-=1
        # print()

    
