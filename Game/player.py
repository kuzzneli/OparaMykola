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




    # Варто було б дописати те, як буде додаватись нова частинка тіла змійки при з'їданні їжі
    # def addCube(self):
    #     self.cubes.append(Cube(self))
    def movePlayer(self):
        # Тут відбувається перевірка на те, куди варто повернути змійці та на яку відстань піти
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

        # Змінюємо сторону, в яку ми маємо йти, в залежності від self.direction
        self.cubes[0].fx = self.cubes[0].posX + self.directionPosX
        self.cubes[0].fy = self.cubes[0].posY + self.directionPosY
        # Рухаємо голову змійки
        self.cubes[0].move(self.cubes[0].fx + self.directionPosX, self.cubes[0].fy + self.directionPosY)
        # Рухаємо решту змійки
        for i in range(1, len(self.cubes)):
            self.cubes[i].move(self.cubes[i - 1].posX, self.cubes[i - 1].posY)

    # Малюємо тіло змійки
    def drawPlayer(self, screen):
        for i in self.cubes:
            pygame.draw.rect(screen, 'red', i.cube)
