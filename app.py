import pygame
from apps.reader import json_parser
from apps.event import event_handler
from apps.audio import audio_handler
from apps.display import print_display
from apps.display import mouth_movement
import time
clock = pygame.time.Clock()
FPS = 120
frames = FPS / 12

# Defining start file
current_file = 'system/json_example.json'

# pygame class init
pygame.init()

# Creating our window
window = pygame.display.set_mode((645, 365))
pygame.display.set_caption('VA-11 HALL-A')

# Init global vars
previousSound = ''
previousName = ''
previousSprite = ''
myfont = pygame.font.SysFont("arial", 15)
ui = pygame.image.load("media/ui/interface.png")
bg = pygame.image.load("media/ui/dynamic_bg.png")
icon = pygame.image.load("media/ui/icon.png")
low_voice = pygame.mixer.Sound("media/sfx/bleep_low.ogg")
low_voice.set_volume(.2)
pygame.display.set_icon(icon)

is_start = 1
score = 0
i = 0
j = 0
c_m_sprite = 0
# Parsing first default file
json_obj = json_parser(current_file)

# Main loop
while is_start:
    # Song load
    if 'music' in json_obj['scenes'][i] and previousSound != json_obj['scenes'][i]['music']:
        audio_handler(json_obj['scenes'][i]['music'], pygame)
        previousSound = json_obj['scenes'][i]['music']

    # Setting current phrase length
    current_phrase_len = len(json_obj['scenes'][i]['text'])

    # Event handling in here
    value_event = event_handler(pygame.event.get())
    if value_event == 'QUIT':
        is_start = 0
    if value_event == 'LEFT_CLICK':
        if i < (len(json_obj['scenes']) - 1):
            if j < current_phrase_len:
                j = current_phrase_len
            else:
                i += 1
                j = 0
        elif 'next_file' in json_obj and i == len(json_obj['scenes']) - 1:
            i = 0
            j = 0
            json_obj = json_parser('system/' + json_obj['next_file'])

    # Display game
    if j < current_phrase_len:
        j += 2
        low_voice.play(-1)
    else:
        low_voice.stop()

    if 'sprite' in json_obj['scenes'][i]:
        previousSprite = print_display(window, pygame, json_obj['scenes'][i], bg, ui, myfont, j)
        if j < current_phrase_len and json_obj['scenes'][i]['name'] != 'Jill':
            c_m_sprite = mouth_movement(window, pygame, json_obj['scenes'][i]['sprite'], c_m_sprite)
    else:
        print_display(window, pygame, json_obj['scenes'][i], bg, ui, myfont, j, previousSprite)
        if j < current_phrase_len and json_obj['scenes'][i]['name'] != 'Jill':
            c_m_sprite = mouth_movement(window, pygame, previousSprite, c_m_sprite)
    time.sleep(.100)
    clock.tick(FPS)

    # Making the character close his eyes randomly, because why not
