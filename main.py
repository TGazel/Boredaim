import pygame

import board
import piece

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Temporary
    screen.fill("purple")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limit FPS to 60

pygame.quit()