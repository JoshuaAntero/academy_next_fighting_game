import pygame

e_head = pygame.image.load('elephant_head.png')
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



def draw_stick_figure_standing(screen, x, y):

    global head
    global l_upperleg
    global l_lowerleg
    global r_upperleg
    global r_lowerleg
    global upperbody
    global lowerbody
    global r_upperarm
    global r_loewrarm
    global l_upperarm
    global l_lowerarm

    # Head
    head = pygame.draw.circle(screen, BLACK, [90 + x, 40 + y ], 30, 1)

    # Left Leg
    l_upperleg = pygame.draw.line(screen, BLACK, [78 + x, 175 + y], [65 + x, 225 + y], 2)
    l_lowerleg = pygame.draw.line(screen, BLACK, [65+ x, 225+y] , [65+x, 275 + y], 2)
    # Right Leg
    r_upperleg = pygame.draw.line(screen, BLACK, [100 + x, 175 + y], [113 + x, 225 + y], 2)
    r_lowerleg = pygame.draw.line(screen, BLACK, [113 + x, 225+y], [113+x, 275+y],2)

    # Body
    #pygame.draw.rect(screen, RED, (0 + x, 0 + y, 200, 300), 1)
    upperbody = pygame.draw.rect(screen, RED, (50 + x, 70 + y, 80, 60), 1)
    lowerbody = pygame.draw.rect(screen, RED, (67 + x, 130 + y, 45, 45), 1)

    # Right Arm
    r_upperarm = pygame.draw.line(screen, RED, [130 + x, 80 + y], [140 + x, 135 + y], 2)
    r_lowerarm = pygame.draw.line(screen, RED, [140 + x, 135 + y], [140 + x, 185 + y], 2)

    # Left Arm
    l_upperarm = pygame.draw.line(screen, RED, [49 + x, 80 + y], [39 + x, 135 + y], 2)
    l_lowerarm = pygame.draw.line(screen, RED, [39 + x, 135 + y], [39 + x, 185 + y], 2)





def character_load(load_number):
    if load_number == 1:
        head = head.blit(elephant_head, (x, y))

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [1024, 576]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # --- Game Logic

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_stick_figure_standing(screen, x_coord, y_coord)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
