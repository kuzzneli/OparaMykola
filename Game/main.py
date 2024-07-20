import pygame
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
player_pos = [620, 480]
p = pygame.Rect(0, 0, 150, 150)
player = pygame.Rect(player_pos[0]-25, player_pos[1]-25, player_pos[0]+25, player_pos[1]+25)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    playerColor = 'red'
    if player.colliderect(p):
        playerColor = 'green'
    pygame.draw.rect(screen, "blue", p)
    pygame.draw.rect(screen, playerColor, player)
    player.update(player_pos[0]-25, player_pos[1]-25, 50,50)

    print(player_pos[0]-25, player_pos[1]-25, player_pos[0]+25, player_pos[1]+25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos[1] -= 300 * dt
    if keys[pygame.K_s]:
        player_pos[1] += 300 * dt
    if keys[pygame.K_a]:
        player_pos[0] -= 300 * dt
    if keys[pygame.K_d]:
        player_pos[0] += 300 * dt
    screen.blit(text_surface, (640, 480))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
