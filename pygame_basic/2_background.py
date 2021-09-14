import pygame

pygame.init()   # initialize; essential function

# set the size of the screen
screen_width = 480      # horizontal size
screen_height = 640     # vertical size
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Nado2_game ")

# load background image
background = pygame.image.load("/home/kyle/PycharmProjects/pyProj/pygame_basic/bg.jpg")

# event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0)) # draw background
    # screen.fill((0, 0, 255))
    pygame.display.update()
# exit pygame
pygame.quit()
