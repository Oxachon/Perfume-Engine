import pygame
from apps.reader import json_parser
from apps.event import event_handler
from apps.audio import audio_handler
from apps.display import print_display

# Defining start file
current_file = 'system/json_example.json'

# pygame class init
pygame.init()

# Creating our window
window = pygame.display.set_mode((1280, 720))

# Init static vars
previousSound = ''
myfont = pygame.font.SysFont("arial", 20)
ui = pygame.image.load("media/ui/messagebox.png")

is_start = 1
score = 0
i = 0
j = 0
# Parsing first default file
json_obj = json_parser(current_file)

# Main loop
while is_start:
    # Song load
    if (json_obj['scenes'][i]['music'] != '' or json_obj['scenes'][i]['music'] is not None) \
            and previousSound != json_obj['scenes'][i]['music']:
        audio_handler(json_obj['scenes'][i]['music'], pygame)
        previousSound = json_obj['scenes'][i]['music']
    current_phrase_len = len(json_obj['scenes'][i]['text'])
    # Event handling in here
    value_event = event_handler(pygame.event.get())
    if value_event == 'QUIT':
        is_start = 0
    if value_event == 'LEFT_CLICK':
        if i < len(json_obj['scenes'])-1:
            if j < current_phrase_len:
                j = current_phrase_len
            else:
                i += 1
                j = 0
        elif json_obj['next_file'] is not None and i == len(json_obj['scenes'])-1:
            i = 0
            j = 0
            json_obj = json_parser('system/'+json_obj['next_file'])

    # Display game
    if j < current_phrase_len:
        j += 1
    print_display(window, pygame, json_obj['scenes'][i], ui, myfont, j)

