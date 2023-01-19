import pygame
pygame.init()
import random

SCR_WD = 800
SCR_HT = 600

UOP = [380,10]
LOP = [149.06, 410]
ROP = [610.94, 410]

def random_point():
    rpx = random.uniform(0.1, (SCR_WD-0.1))
    rpy = random.uniform(0.1, (SCR_WD-0.1))
    rp = [rpx, rpy]
    return rp

def midpoint(first_point, second_point):
    rpx = (first_point[0] + second_point[0]) / 2.0
    rpy = (first_point[1] + second_point[1]) / 2.0
    rp = [rpx, rpy]
    return rp

def select_original():
    options = [UOP, LOP, ROP]
    chosen = random.choice(options)
    return chosen

def generate_many_points(n):
    all_points = [[]]
    all_points[0] = random_point()
    while len(all_points) < n:
        npa = select_original()
        np = midpoint(all_points[-1], npa)
        all_points.append(np)
    return all_points

hundred_points = generate_many_points(1000)

# Set up the drawing window
screen = pygame.display.set_mode([SCR_WD, SCR_HT])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    #draw the first three points in red
    pygame.draw.circle(screen, (255,0,0), (UOP[0],UOP[1]), 2)
    pygame.draw.circle(screen, (255,0,0), (LOP[0],LOP[1]), 2)
    pygame.draw.circle(screen, (255,0,0), (ROP[0],ROP[1]), 2)

    #draw the hundred points in blue
    for dot in hundred_points:
        pygame.draw.circle(screen, (0,0,255), (dot[0],dot[1]), 2)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
