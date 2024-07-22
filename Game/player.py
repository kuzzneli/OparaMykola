import pygame.draw
from TimeModule import Time
from cubes import Cube
import time

class Player:
    cubes = []

    def __init__(self, x, y):

        self.direction = 0
        self.directionPosX = 25
        self.directionPosY = 0
        self.cubes.append(Cube(x, y, x + self.directionPosX, y + self.directionPosY))





    # def addCube(self):
    #     self.cubes.append(Cube(self))
    def movePlayer(self):
        if self.direction == 0:
            self.directionPosX = 25
            self.directionPosY = 0
        if self.direction == 1:
            self.directionPosX = 0
            self.directionPosY = 25
        if self.direction == 2:
            self.directionPosX = -25
            self.directionPosY = 0
        if self.direction == 3:
            self.directionPosX = 0
            self.directionPosY = -25
        self.cubes[0].fx = self.cubes[0].posX + self.directionPosX
        self.cubes[0].fy = self.cubes[0].posY + self.directionPosY
        self.cubes[0].move(self.cubes[0].fx + self.directionPosX, self.cubes[0].fy + self.directionPosY)
        for i in range(1, len(self.cubes)):
            self.cubes[i].move(self.cubes[i - 1].posX, self.cubes[i - 1].posY)

    def drawPlayer(self, screen):
        for i in self.cubes:
            pygame.draw.rect(screen, 'red', i.cube)
