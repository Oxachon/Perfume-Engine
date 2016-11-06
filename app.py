import pygame
from pygame.locals import *

# pygame class init
pygame.init()

# Init sound
sound = pygame.mixer.Sound("media/music/bgm01.ogg")

# Creating our window
window = pygame.display.set_mode((1280, 720))

# Background first
bg = pygame.image.load("media/background/bg1")
window.blit(bg, (0,0))

# Then comes the character
character = pygame.image.load("media/characters/himu1")
window.blit(character, (400,0))

# The UI is the last fo be blitz
ui = pygame.image.load("media/ui/messagebox.png")
window.blit(ui, (5,420))

# Refreshing the display with all the layers set
pygame.display.flip()

# starting music
sound.play()

is_start = 1

# Main loop
while is_start:
	for event in pygame.event.get():   
		if event.type == QUIT:     
			is_start = 0
            # sound.stop()