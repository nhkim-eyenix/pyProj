import pygame

pygame.init()   # initialize; essential function

# set the size of the screen
screen_width = 480      # horizontal size
screen_height = 640     # vertical size
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Nado3_game ")

# load background image
background = pygame.image.load("/home/kyle/PycharmProjects/pyProj/pygame_basic/bg2.jpg")

# Load Character(Sprite)
character = pygame.image.load("/home/kyle/PycharmProjects/pyProj/pygame_basic/character.jpg")
character_size = character.get_rect().size # get image's size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = dscreen_width / 2
character_y_pos = screen_height



# event loop
running = True # Is the game running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0)) # draw background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()
# exit pygame
pygame.quit()
