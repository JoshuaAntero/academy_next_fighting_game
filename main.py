import pygame

walkRight = pygame.image.load('stickmanWalk.png')
walkLeft = pygame.transform.flip(walkRight, 1, 0)
kickRight = pygame.image.load('stickmanKick.png')
kickLeft = pygame.transform.flip(kickRight, 1, 0)
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Game")

over = False
x = 0
y = 400
speed = 1
flip = False
kicking = False
black = [255,255,255]

def checkMovement():

    global x
    global flip
    global kicking

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        flip = True
        x -= speed

    if keys[pygame.K_RIGHT]:
        flip = False
        x += speed

    if keys[pygame.K_a]:
        if not flip:
            screen.blit(kickRight, (x, y))
        else:
            screen.blit(kickLeft, (x - 50, y))


while not over:

    pygame.time.delay(5)
    screen.fill([255, 255, 255])

    if flip:
        screen.blit(walkLeft, (x, y))

    else:
        screen.blit(walkRight, (x, y))

    checkMovement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True

    pygame.display.flip()
