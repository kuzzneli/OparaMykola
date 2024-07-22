import time

import pygame

from Game.TimeModule import Time
from player import Player
from Extra import Extra
# pygame setup
pygame.font.init()
pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

score = 0

text_surface = my_font.render(f'Score: {score}', False, (0, 0, 0))
player = Player(620, 480)
myTime = time.time()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    # Змінюємо напрям, в якому буде ходити змійка
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.direction = 3
    if keys[pygame.K_s]:
        player.direction = 1
    if keys[pygame.K_a]:
        player.direction = 2
    if keys[pygame.K_d]:
        player.direction = 0
    screen.blit(text_surface, (640, 480))

    newTime = time.time()
    if newTime - myTime > 0.5:
        player.movePlayer()
        myTime = newTime

    player.drawPlayer(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
