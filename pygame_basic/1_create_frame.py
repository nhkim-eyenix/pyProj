import pygame

pygame.init()   # initialize; essential function

# set the size of the screen
screen_width = 480      # horizontal size
screen_height = 640     # vertical size
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Nado_game")

# event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#exit pygame
pygame.quit()
