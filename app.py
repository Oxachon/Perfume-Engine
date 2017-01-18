import pygame
from apps.reader import json_parser
from apps.event import event_handler
from apps.audio import audio_handler

# Defining start file
start_file = 'system/json_example.json'

# pygame class init
pygame.init()

# Creating our window
window = pygame.display.set_mode((1280, 720))

# Init static vars
previousSound = ''


# Init sound
myfont = pygame.font.SysFont("arial", 20)
ui = pygame.image.load("media/ui/messagebox.png")

is_start = 1
score = 0
i = 0
# Main loop
while is_start:
    json_obj = json_parser(start_file)

    # Song load
    if (json_obj['scenes'][i]['music'] != '' or json_obj['scenes'][i]['music'] is not None) and previousSound != json_obj['scenes'][i]['music']:
        audio_handler(json_obj['scenes'][i]['music'], pygame)
        previousSound = json_obj['scenes'][i]['music']


    # Refilling to empty current space
    window.fill(pygame.Color("white"))

    # Background first
    bg = pygame.image.load("media/background/"+json_obj['scenes'][i]['background'])
    window.blit(bg, (0, 0))

    # Then comes the character
    character = pygame.image.load("media/characters/"+json_obj['scenes'][i]['character'])
    window.blit(character, (400, 0))

    # The UI is the last fo be blitz
    window.blit(ui, (5, 420))

    value_event = event_handler(pygame.event.get())
    if value_event == 'QUIT':
        is_start = 0
    if value_event == 'LEFT_CLICK':
        if i < len(json_obj['scenes'])-1:
            i += 1

    score = json_obj['scenes'][i]['text']
    label = myfont.render(score, 1, (0, 0, 0))
    window.blit(label, (100, 560))
    # Refreshing the display with all the layers set
    pygame.display.flip()
