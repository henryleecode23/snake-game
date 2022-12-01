import pygame
import sys
from core import game_map
from core.text import Text
from typing import List
# from utils.handler.logging import Logger


class Game():
    def __init__(self):
        # Logger.msg("Loading files...")
        pygame.init()
        pygame.font.init()
        self.mainWindow = pygame.display.set_mode((600, 700))
        self.clock = pygame.time.Clock()
        self.size = 15
        self.position = [7, 7]
        self.defaultLenth = 5
        self.lenth = self.defaultLenth
        self.gameMap = game_map.GameMap(self.size, tuple(self.position))
        for i in range(self.lenth):
            self.gameMap.table[7][7-i] = self.lenth - i
            print(f"set (7, {8-i}) = {self.lenth-1-i}")
        self.pixelPerBlock = 40
        self.MAXFPS = 60
        # self.difficulty = 156
        self.direction = "RIGHT"
        self.actTime = 30
        self.moveTime = 60
        self.gg = False
        self.renderText = []
        self.renderText:List[Text]

    def restart(self):
        self.size = 15
        self.position = [7, 7]
        self.gameMap = game_map.GameMap(self.size, tuple(self.position))
        self.lenth = self.defaultLenth
        for i in range(1, self.defaultLenth +1):
            self.gameMap.table[7][8-i] = self.defaultLenth -1 - i
            print(f"set (7, {8-i}) = {self.defaultLenth-1-i}")
        # self.gameMap.table[7][5] = 1
        # self.gameMap.table[7][6] = 2
        # self.gameMap.table[7][7] = 3
        self.pixelPerBlock = 40
        self.MAXFPS = 60
        # self.difficulty = 156
        self.direction = "RIGHT"
        self.actTime = 30
        self.moveTime = 60
        self.gg = False
        self.renderText = []
        self.renderText:List[Text]

    def run(self):
        while True:
            self.clock.tick(self.MAXFPS) 
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.direction != "UP":
                        self.direction = "DOWN"
                    if (keys[pygame.K_UP] or keys[pygame.K_w])and self.direction != "DOWN":
                        self.direction = "UP"
                    if (keys[pygame.K_LEFT] or keys[pygame.K_a])and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    if (keys[pygame.K_RIGHT] or keys[pygame.K_d])and self.direction != "LEFT":
                        self.direction = "RIGHT"
            
            self.actTime+=1
            if self.actTime >= self.moveTime:
                self.gameMap.action()
                if self.direction == "UP":
                    self.position[0]-=1
                elif self.direction == "DOWN":
                    self.position[0]+=1
                elif self.direction == "LEFT":
                    self.position[1]-=1
                elif self.direction == "RIGHT":
                    self.position[1]+=1

                if (self.position[0] < 0 or self.position[0] >= self.size or self.position[1] < 0 or self.position[1] >= self.size or self.gameMap.table[self.position[0]][self.position[1]] > 0):
                    self.renderText.append(Text("Game Over", (300, 10), (0, 0, 0)))
                    self.renderText.append(Text("Press any key to play again", (300, 70), (0, 0, 0)))
                    self.gg = True
                    while self.gg:
                        self.clock.tick(self.MAXFPS)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                self.restart()


                        for text in self.renderText:
                            text.render(self.mainWindow)
                        pygame.display.update()

                self.gameMap.table[self.position[0]][self.position[1]] = self.lenth
                self.actTime = 0
            
            
                                        
            # the latest background
            self.mainWindow.fill((255, 255, 255))
            pygame.draw.rect(self.mainWindow, (0, 0, 0), pygame.Rect(0, 100, 600, 600))

            # game map background
            for i in range(self.size):
                for j in range(self.size):
                    block = pygame.Rect(5+j*self.pixelPerBlock, 5+i*self.pixelPerBlock+100, self.pixelPerBlock-10, self.pixelPerBlock-10)
                    pygame.draw.rect(self.mainWindow, (50, 50, 50), block)
            
            # item on game map
            for i in range(self.size):
                for j in range(self.size):
                    # blank
                    if self.gameMap.table[i][j] == 0:
                        continue
                    # snake head
                    if self.gameMap.table[i][j] == self.lenth:
                        block = pygame.Rect(j*self.pixelPerBlock, i*self.pixelPerBlock+100, self.pixelPerBlock, self.pixelPerBlock)
                        pygame.draw.rect(self.mainWindow, (0, 0, 240), block)
                        continue
                    # snake body
                    if self.gameMap.table[i][j] > 0:
                        block = pygame.Rect(j*self.pixelPerBlock, i*self.pixelPerBlock+100, self.pixelPerBlock, self.pixelPerBlock)
                        pygame.draw.rect(self.mainWindow, (0, 200, 200), block)
                        continue
            
            pygame.display.update()

            
            

