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
    
    @property
    def startPoint(self):
        return self._startPoint
    
    @startPoint.setter
    def startPoint(self, Point:Tuple[int, int]):
        x, y = Point[0], Point[1] 
        if ( x < 0 or y < 0 or x > self.size or y > self.size):
            return Logger.error(f"the x and y positions must between 0~{self.size}.")
        self._startPoint = (x, y)

    def action(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.table[i][j] <= 0:
                    continue
                self.table[i][j]-=1


    
