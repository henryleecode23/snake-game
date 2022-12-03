import pygame
import sys
from core import game_map
from core.text import Text
from typing import List
from random import randint


class Game():
    def __init__(self):
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
        self.gameMap.table[7][self.size-2] = -1
        self.pixelPerBlock = 40
        self.MAXFPS = 60
        self.direction = "RIGHT"
        self.actTime = 30
        self.defaultMoveTime = 60
        self.moveTime = self.defaultMoveTime
        self.gg = False
        self.renderText = []
        self.renderText:List[Text]
        self.pointRespawn = False
        self.score = 0
        self.lastDirection = "RIGHT"
        self.nextDirection = "RIGHT"

    def restart(self):
        self.size = 15
        self.position = [7, 7]
        self.defaultLenth = 3
        self.lenth = self.defaultLenth
        self.gameMap.reset()
        for i in range(self.lenth):
            self.gameMap.table[7][7-i] = self.lenth - i
        self.gameMap.table[7][self.size-2] = -1
        self.pixelPerBlock = 40
        self.MAXFPS = 60
        self.direction = "RIGHT"
        self.actTime = 30
        self.moveTime = self.defaultMoveTime
        self.gg = False
        self.renderText = []
        self.renderText:List[Text]
        self.pointRespawn = False
        self.score = 0
        self.nextDirection = "RIGHT"

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
                        self.nextDirection = "DOWN"
                    if (keys[pygame.K_UP] or keys[pygame.K_w])and self.direction != "DOWN":
                        self.nextDirection = "UP"
                    if (keys[pygame.K_LEFT] or keys[pygame.K_a])and self.direction != "RIGHT":
                        self.nextDirection = "LEFT"
                    if (keys[pygame.K_RIGHT] or keys[pygame.K_d])and self.direction != "LEFT":
                        self.nextDirection = "RIGHT"
            
            self.actTime+=1
            if self.actTime >= self.moveTime:
                self.gameMap.action()
                self.direction = self.nextDirection
                if self.direction == "UP":
                    self.position[0]-=1
                elif self.direction == "DOWN":
                    self.position[0]+=1
                elif self.direction == "LEFT":
                    self.position[1]-=1
                elif self.direction == "RIGHT":
                    self.position[1]+=1

                # game over loop
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
                
                # get point
                if self.gameMap.table[self.position[0]][self.position[1]] == -1:
                    self.pointRespawn = True
                    # respawn point            
                    while self.pointRespawn:
                        x, y =randint(0, self.size-1), randint(0, self.size-1)
                        if self.gameMap.table[x][y] == 0:
                            self.gameMap.table[x][y] = -1
                            self.score += 1
                            self.lenth += 1
                            if self.moveTime > 5:
                                # 0~5: 4
                                # 6~10: 3
                                # 11~15: 2
                                # 16~ : 1
                                if self.score > 16:
                                    self.moveTime -= 1
                                elif self.score > 11:
                                    self.moveTime -= 2
                                elif self.score > 6:
                                    self.moveTime -= 3
                                elif self.score > 4:
                                    self.moveTime -= 4
                            self.pointRespawn = False
                
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
                    # point
                    elif self.gameMap.table[i][j] == -1:
                        block = pygame.Rect(j*self.pixelPerBlock, i*self.pixelPerBlock+100, self.pixelPerBlock, self.pixelPerBlock)
                        pygame.draw.rect(self.mainWindow, (200, 0, 0), block)
                        continue
                    # snake head
                    elif self.gameMap.table[i][j] == self.lenth:
                        block = pygame.Rect(j*self.pixelPerBlock, i*self.pixelPerBlock+100, self.pixelPerBlock, self.pixelPerBlock)
                        pygame.draw.rect(self.mainWindow, (0, 0, 240), block)
                        continue
                    # snake body
                    elif self.gameMap.table[i][j] > 0:
                        block = pygame.Rect(j*self.pixelPerBlock, i*self.pixelPerBlock+100, self.pixelPerBlock, self.pixelPerBlock)
                        pygame.draw.rect(self.mainWindow, (0, 200, 200), block)
                        continue
            
            
            
            self.renderText.append(Text(f"Score: {self.score}", (10, 10), (0, 0, 0)))
            for _ in range(len(self.renderText)):
                self.renderText.pop().render(self.mainWindow)
                

            
            pygame.display.update()

            
            

