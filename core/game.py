import pygame
import sys
from core import game_map
# from utils.handler.logging import Logger


class Game():
    def __init__(self):
        # Logger.msg("Loading files...")
        pygame.init()
        self.mainWindow = pygame.display.set_mode((600, 700))
        self.clock = pygame.time.Clock()
        self.size = 15
        self.position = [7, 7]
        self.gameMap = game_map.GameMap(self.size, tuple(self.position))
        self.pixelPerblock = 600/15
        self.MAXFPS = 60
        # self.difficulty = 156
        self.direction = "RIGHT"
        self.lenth = 3
        self.actTime = 30


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
            if self.actTime >= 30:
                self.gameMap.action()
                if self.direction == "UP":
                    self.position[0]-=1
                elif self.direction == "DOWN":
                    self.position[0]+=1
                elif self.direction == "LEFT":
                    self.position[1]-=1
                elif self.direction == "RIGHT":
                    self.position[1]+=1
                self.gameMap.table[self.position[0]][self.position[1]] = self.lenth
                self.actTime = 0
            
            self.mainWindow.fill((255, 255, 255))
            pygame.draw.rect(self.mainWindow, (0, 0, 0), pygame.Rect(0, 100, 600, 600))

            for i in range(self.size):
                for j in range(self.size):
                    block = pygame.Rect(5+j*self.pixelPerblock, 5+i*self.pixelPerblock+100, self.pixelPerblock-10, self.pixelPerblock-10)
                    pygame.draw.rect(self.mainWindow, (50, 50, 50), block)
            
            for i in range(self.size):
                for j in range(self.size):
                    if self.gameMap.table[i][j] == 0:
                        continue
                    if self.gameMap.table[i][j] > 0:
                        block = pygame.Rect(j*self.pixelPerblock, i*self.pixelPerblock+100, self.pixelPerblock, self.pixelPerblock)
                        pygame.draw.rect(self.mainWindow, (0, 200, 200), block)
                        continue
                    # if self.gameMap.table[i][j] == -1:
                    #     block = pygame.Rect(1+j*self.pixelPerblock, 1+i*self.pixelPerblock, self.pixelPerblock, self.pixelPerblock)
                    #     pygame.draw.rect(self.mainWindow, (100, 0, 0), block)
            
            pygame.display.update()

            
            

