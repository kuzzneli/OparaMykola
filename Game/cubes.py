from pygame import Rect


class Cube:
    def __init__(self, posx, posy, fx, fy):
        self.posX = posx
        self.posY = posy
        self.fx = fx
        self.fy = fy
        self.cube = Rect(self.posX - 12.5, self.posY - 12.5, 25, 25)

    def move(self, fx, fy):
        self.posX = self.fx
        self.posY = self.fy
        self.fx = fx
        self.fy = fy
        self.cube.update(self.posX - 12.5, self.posY - 12.5, 25, 25)
