import pygame


class Extra:
    objects = []

    def __init__(self):
        pass

    def addObject(self, object):
        self.objects.append(object)
        self.drawAll()
    def drawAll(self):
        for obj in self.objects:
            if obj.type == 'circle':
                pygame.draw.circle(obj.screen, obj.color, obj.playerPos, obj.size)