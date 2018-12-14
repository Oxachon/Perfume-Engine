from pygame.constants import *


def event_handler(main_event):
    for event in main_event:
        if event.type == QUIT:
            return 'QUIT'
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                return 'LEFT_CLICK'
            else:
                return 'RIGHT_CLICK'
